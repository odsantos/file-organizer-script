from datetime import datetime, date, timedelta
from enum import Enum
import os
import re
import shutil
import json

class FileProperty(Enum):
    """Enum for file properties that can be evaluated."""
    FileName = "FileName"
    FileExtension = "FileExtension"
    CreationDate = "CreationDate"
    LastModifiedDate = "LastModifiedDate"
    FileSize = "FileSize"
    ExifDateTaken = "ExifDateTaken" # Requires external library for EXIF

class Operator(Enum):
    """Enum for comparison operators."""
    Equals = "Equals"
    Contains = "Contains"
    StartsWith = "StartsWith"
    EndsWith = "EndsWith"
    MatchesRegex = "MatchesRegex"
    GreaterThan = "GreaterThan"
    LessThan = "LessThan"
    IsOlderThan = "IsOlderThan" # Value is timedelta
    IsNewerThan = "IsNewerThan" # Value is timedelta

class LogicOperator(Enum):
    """Enum for combining multiple conditions."""
    AND = "AND"
    OR = "OR"

class ActionType(Enum):
    """Enum for types of actions a rule can perform."""
    Move = "Move"
    Rename = "Rename"
    Copy = "Copy"
    Delete = "Delete"

class ScheduleType(Enum):
    """Enum for scheduling types."""
    Daily = "Daily"
    Weekly = "Weekly"
    Monthly = "Monthly"
    Once = "Once"
    Manual = "Manual"

class Condition:
    """Represents a single criterion for a file."""
    def __init__(self, file_property: FileProperty, operator: Operator, value):
        self.file_property = file_property
        self.operator = operator
        self.value = value

    def evaluate(self, file_path: str) -> bool:
        """
        Evaluates the condition against the given file path.
        """
        stat = os.stat(file_path)
        file_name, file_extension = os.path.splitext(os.path.basename(file_path))

        actual_value = None

        if self.file_property == FileProperty.FileName:
            actual_value = file_name
        elif self.file_property == FileProperty.FileExtension:
            actual_value = file_extension.lstrip('.') # Remove leading dot
        elif self.file_property == FileProperty.CreationDate:
            actual_value = datetime.fromtimestamp(stat.st_ctime)
        elif self.file_property == FileProperty.LastModifiedDate:
            actual_value = datetime.fromtimestamp(stat.st_mtime)
        elif self.file_property == FileProperty.FileSize:
            actual_value = stat.st_size
        elif self.file_property == FileProperty.ExifDateTaken:
            # TODO: Implement EXIF data extraction using an external library (e.g., Pillow)
            # For now, return False as it cannot be evaluated
            return False

        if actual_value is None:
            return False

        # --- Evaluate based on operator ---
        if self.operator == Operator.Equals:
            return actual_value == self.value
        elif self.operator == Operator.Contains:
            return self.value in actual_value
        elif self.operator == Operator.StartsWith:
            return actual_value.startswith(self.value)
        elif self.operator == Operator.EndsWith:
            return actual_value.endswith(self.value)
        elif self.operator == Operator.MatchesRegex:
            if isinstance(actual_value, str):
                return bool(re.search(self.value, actual_value))
            return False # Regex only applies to strings
        elif self.operator == Operator.GreaterThan:
            return actual_value > self.value
        elif self.operator == Operator.LessThan:
            return actual_value < self.value
        elif self.operator == Operator.IsOlderThan:
            # Value is timedelta, actual_value is datetime
            # Check if actual_value is older than (now - self.value)
            return actual_value < (datetime.now() - self.value)
        elif self.operator == Operator.IsNewerThan:
            # Value is timedelta, actual_value is datetime
            # Check if actual_value is newer than (now - self.value)
            return actual_value > (datetime.now() - self.value)

        return False # Should not reach here
    
    def to_dict(self):
        value = self.value
        if isinstance(value, (datetime, date)):
            value = value.isoformat()
        elif isinstance(value, timedelta):
            value = value.total_seconds() # Store timedelta as seconds
        return {
            "file_property": self.file_property.value,
            "operator": self.operator.value,
            "value": value
        }

    @classmethod
    def from_dict(cls, data):
        value = data["value"]
        if data["operator"] in [Operator.IsOlderThan.value, Operator.IsNewerThan.value]:
            value = timedelta(seconds=value)
        elif "Date" in data["file_property"]: # Generic check for date properties
            try:
                value = datetime.fromisoformat(value)
            except ValueError:
                pass # If it's not an isoformat date, keep as is (e.g. for placeholders)
        return cls(FileProperty(data["file_property"]), Operator(data["operator"]), value)


class Action:
    """Represents an operation to perform on a file when a rule is triggered."""
    def __init__(self, action_type: ActionType, destination: str = None, pattern: str = None):
        self.action_type = action_type
        self.destination = destination
        self.pattern = pattern

    def execute(self, file_path: str, placeholders: dict) -> bool:
        """
        Executes the action on the given file.
        Returns True on success, False otherwise.
        """
        try:
            if self.action_type == ActionType.Move:
                if self.destination:
                    # Apply placeholders to destination
                    formatted_destination = self._format_path(self.destination, placeholders)
                    
                    # Ensure destination directory exists
                    os.makedirs(os.path.dirname(formatted_destination), exist_ok=True)
                    shutil.move(file_path, formatted_destination)
                    return True
            elif self.action_type == ActionType.Rename:
                if self.pattern:
                    # Apply placeholders to new file name
                    new_name = self._format_path(self.pattern, placeholders)
                    new_file_path = os.path.join(os.path.dirname(file_path), new_name)
                    os.rename(file_path, new_file_path)
                    return True
            # TODO: Implement Copy and Delete actions
            return False
        except Exception as e:
            print(f"Error executing action {self.action_type.value} on {file_path}: {e}")
            return False

    def _format_path(self, path_template: str, placeholders: dict) -> str:
        """
        Formats a path string using provided placeholders.
        """
        # Ensure that values in placeholders are strings before formatting
        stringified_placeholders = {k: str(v) for k, v in placeholders.items()}
        return path_template.format(**stringified_placeholders)
    
    def to_dict(self):
        return {
            "action_type": self.action_type.value,
            "destination": self.destination,
            "pattern": self.pattern
        }

    @classmethod
    def from_dict(cls, data):
        return cls(ActionType(data["action_type"]), data["destination"], data["pattern"])


class Schedule:
    """Defines the automatic execution timing for a rule."""
    def __init__(self, schedule_type: ScheduleType, time: datetime.time = None, day_of_week: Enum = None, 
                 day_of_month: int = None, date: date = None):
        self.schedule_type = schedule_type
        self.time = time
        self.day_of_week = day_of_week
        self.day_of_month = day_of_month
        self.date = date

    def to_dict(self):
        time_str = self.time.isoformat() if self.time else None
        day_of_week_str = self.day_of_week.value if self.day_of_week else None
        date_str = self.date.isoformat() if self.date else None
        return {
            "schedule_type": self.schedule_type.value,
            "time": time_str,
            "day_of_week": day_of_week_str,
            "day_of_month": self.day_of_month,
            "date": date_str
        }

    @classmethod
    def from_dict(cls, data):
        time_obj = datetime.fromisoformat(data["time"]).time() if data["time"] else None
        day_of_week_obj = Enum(data["day_of_week"]) if data["day_of_week"] else None # Assuming Enum for day_of_week
        date_obj = date.fromisoformat(data["date"]) if data["date"] else None
        return cls(ScheduleType(data["schedule_type"]), time_obj, day_of_week_obj, data["day_of_month"], date_obj)


class Rule:
    """Represents a single automated organization rule."""
    def __init__(self, name: str, conditions: list[Condition], logic_operator: LogicOperator = LogicOperator.AND,
                 actions: list[Action] = None, schedule: Schedule = None, description: str = "", enabled: bool = True):
        self.name = name
        self.description = description
        self.enabled = enabled
        self.conditions = conditions
        self.logic_operator = logic_operator
        self.actions = actions if actions is not None else []
        self.schedule = schedule
        self.last_run = None # datetime

    def evaluate(self, file_path: str) -> bool:
        """
        Evaluates all conditions of the rule against the given file path
        and combines the results using the specified logical operator.
        """
        if not self.enabled:
            return False

        if not self.conditions:
            return True # No conditions means always true (unconditional action)

        results = [condition.evaluate(file_path) for condition in self.conditions]

        if self.logic_operator == LogicOperator.AND:
            return all(results)
        elif self.logic_operator == LogicOperator.OR:
            return any(results)
        
        return False # Should not reach here

    def execute_actions(self, file_path: str, placeholders: dict = None) -> bool:
        """
        Executes all defined actions for the rule on the given file.
        Returns True if all actions succeed, False otherwise.
        """
        if not self.actions:
            return True # No actions to execute

        all_succeeded = True
        current_file_path = file_path # In case of rename, subsequent actions use new path

        # Prepare base placeholders that are always available
        base_placeholders = {
            "original_name": os.path.splitext(os.path.basename(file_path))[0],
            "extension": os.path.splitext(os.path.basename(file_path))[1].lstrip('.'),
            "YYYY": datetime.now().strftime("%Y"),
            "MM": datetime.now().strftime("%m"),
            "DD": datetime.now().strftime("%d"),
            "HH": datetime.now().strftime("%H"),
            "MI": datetime.now().strftime("%M"),
            "SS": datetime.now().strftime("%S"),
        }
        # Merge with any provided dynamic placeholders (e.g., from keyword match)
        final_placeholders = {**base_placeholders, **(placeholders if placeholders is not None else {})}

        for action in self.actions:
            # For rename action, we need to pass the *current* file_path, which might have changed
            # from a previous rename action within the same rule.
            succeeded = action.execute(current_file_path, final_placeholders)
            if not succeeded:
                all_succeeded = False
                break
            
            # If the action was a rename, update current_file_path for subsequent actions
            if action.action_type == ActionType.Rename and action.pattern:
                new_name = action._format_path(action.pattern, final_placeholders)
                current_file_path = os.path.join(os.path.dirname(current_file_path), new_name)
        
        return all_succeeded
    
    def to_dict(self):
        last_run_str = self.last_run.isoformat() if self.last_run else None
        return {
            "name": self.name,
            "description": self.description,
            "enabled": self.enabled,
            "conditions": [c.to_dict() for c in self.conditions],
            "logic_operator": self.logic_operator.value,
            "actions": [a.to_dict() for a in self.actions],
            "schedule": self.schedule.to_dict() if self.schedule else None,
            "last_run": last_run_str
        }

    @classmethod
    def from_dict(cls, data):
        conditions = [Condition.from_dict(c_data) for c_data in data["conditions"]]
        actions = [Action.from_dict(a_data) for a_data in data["actions"]]
        schedule = Schedule.from_dict(data["schedule"]) if data["schedule"] else None
        last_run = datetime.fromisoformat(data["last_run"]) if data["last_run"] else None
        
        rule = cls(data["name"], conditions, LogicOperator(data["logic_operator"]), actions, schedule,
                   data["description"], data["enabled"])
        rule.last_run = last_run
        return rule

class RuleManager:
    """Manages loading, saving, and executing a collection of rules."""
    def __init__(self, rules_file: str):
        self.rules_file = rules_file
        self.rules: list[Rule] = []
        self._load_rules()

    def _load_rules(self):
        if os.path.exists(self.rules_file):
            with open(self.rules_file, 'r') as f:
                data = json.load(f)
                self.rules = [Rule.from_dict(rule_data) for rule_data in data]
        else:
            self.rules = []

    def save_rules(self):
        with open(self.rules_file, 'w') as f:
            json.dump([rule.to_dict() for rule in self.rules], f, indent=4)

    def add_rule(self, rule: Rule):
        self.rules.append(rule)
        self.save_rules()

    def remove_rule(self, rule_name: str):
        self.rules = [rule for rule in self.rules if rule.name != rule_name]
        self.save_rules()

    def get_rule(self, rule_name: str) -> Rule | None:
        for rule in self.rules:
            if rule.name == rule_name:
                return rule
        return None

    def process_directory(self, directory_path: str):
        """
        Applies all enabled rules to files within the specified directory.
        """
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                for rule in self.rules:
                    if rule.enabled and rule.evaluate(file_path):
                        print(f"Applying rule '{rule.name}' to '{file_path}'")
                        rule.execute_actions(file_path) # Pass potential dynamic placeholders later
                        # If a file is moved/renamed, it might not exist at old path for other rules
                        # For now, we assume once an action is taken, we move to next file.
                        break # Only one rule applies per file for now