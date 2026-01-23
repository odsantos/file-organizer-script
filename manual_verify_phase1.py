import os
import shutil
from datetime import datetime, timedelta
from rules import (
    FileProperty, Operator, LogicOperator, ActionType,
    Condition, Action, Rule, RuleManager, ScheduleType
)

# --- Setup Test Environment ---
test_base_dir = "manual_verification_test_env"
rules_file = os.path.join(test_base_dir, "test_rules.json")
source_dir = os.path.join(test_base_dir, "source")
dest_dir_pdf = os.path.join(test_base_dir, "destination", "PDFs")
dest_dir_images = os.path.join(test_base_dir, "destination", "Images")
dest_dir_archive = os.path.join(test_base_dir, "archive")
dest_dir_reports = os.path.join(test_base_dir, "reports")


# Clean up previous run
if os.path.exists(test_base_dir):
    shutil.rmtree(test_base_dir)

os.makedirs(source_dir, exist_ok=True)
os.makedirs(dest_dir_pdf, exist_ok=True)
os.makedirs(dest_dir_images, exist_ok=True)
os.makedirs(dest_dir_archive, exist_ok=True)
os.makedirs(dest_dir_reports, exist_ok=True)


# Create dummy files
file1_path = os.path.join(source_dir, "document_report_q1.pdf")
file2_path = os.path.join(source_dir, "photo_holiday.jpg")
file3_path = os.path.join(source_dir, "another_doc.docx")
file4_path = os.path.join(source_dir, "old_data.txt")
file5_path = os.path.join(source_dir, "invoice_client_a.pdf")


with open(file1_path, "w") as f: f.write("content")
with open(file2_path, "w") as f: f.write("content")
with open(file3_path, "w") as f: f.write("content")
with open(file4_path, "w") as f: f.write("content")
with open(file5_path, "w") as f: f.write("content")


# Make file4 older for archiving test
old_time = datetime.now() - timedelta(days=90)
os.utime(file4_path, (old_time.timestamp(), old_time.timestamp()))

# --- Define Rules ---

# Rule 1: Move PDFs
rule1_conditions = [
    Condition(FileProperty.FileExtension, Operator.Equals, "pdf")
]
rule1_actions = [
    Action(ActionType.Move, destination=dest_dir_pdf)
]
rule1 = Rule("Move PDFs", rule1_conditions, actions=rule1_actions)

# Rule 2: Move JPGs and Rename
rule2_conditions = [
    Condition(FileProperty.FileExtension, Operator.Equals, "jpg")
]
rule2_actions = [
    Action(ActionType.Rename, pattern="{original_name}_processed.{extension}"),
    Action(ActionType.Move, destination=dest_dir_images)
]
rule2 = Rule("Move & Rename JPGs", rule2_conditions, actions=rule2_actions)

# Rule 3: Archive old TXT files (older than 60 days)
rule3_conditions = [
    Condition(FileProperty.FileExtension, Operator.Equals, "txt"),
    Condition(FileProperty.LastModifiedDate, Operator.IsOlderThan, timedelta(days=60))
]
rule3 = Rule("Archive Old Text Files", rule3_conditions, actions=[Action(ActionType.Move, destination=dest_dir_archive)])

# Rule 4: Move reports containing 'report' in filename
rule4_conditions = [
    Condition(FileProperty.FileName, Operator.Contains, "report")
]
rule4 = Rule("Move Reports", rule4_conditions, actions=[Action(ActionType.Move, destination=dest_dir_reports)])

# Rule 5: Example of OR logic - Move documents OR invoices to PDFs
rule5_conditions = [
    Condition(FileProperty.FileName, Operator.Contains, "doc"),
    Condition(FileProperty.FileName, Operator.Contains, "invoice")
]
rule5 = Rule("Move Docs OR Invoices (OR Logic)", rule5_conditions, LogicOperator.OR, actions=[Action(ActionType.Move, destination=dest_dir_pdf)])


# --- Save Rules ---
manager = RuleManager(rules_file)
manager.add_rule(rule1)
manager.add_rule(rule2)
manager.add_rule(rule3)
manager.add_rule(rule4)
manager.add_rule(rule5)

print(f"Rules saved to {rules_file}")
print("Initial files in source directory:")
print(os.listdir(source_dir))

# --- Process Directory ---
print(f"\nProcessing directory: {source_dir}")
manager.process_directory(source_dir)

# --- Verification ---
print("\n--- Verification ---")

print(f"Files remaining in source directory ({source_dir}):")
print(os.listdir(source_dir)) # Should be empty

print(f"Files in PDF destination ({dest_dir_pdf}):")
print(os.listdir(dest_dir_pdf)) # Should contain document_report_q1.pdf and invoice_client_a.pdf

print(f"Files in Images destination ({dest_dir_images}):")
print(os.listdir(dest_dir_images)) # Should contain photo_holiday_processed.jpg

print(f"Files in Archive destination ({dest_dir_archive}):")
print(os.listdir(dest_dir_archive)) # Should contain old_data.txt

print(f"Files in Reports destination ({dest_dir_reports}):")
print(os.listdir(dest_dir_reports)) # Should contain document_report_q1.pdf (moved by rule 4 or rule 1 if rule 4 fails)

print("\nManual verification setup complete. Please check the directories.")
