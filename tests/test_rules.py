import unittest
import os
import shutil
from datetime import datetime, timedelta

from rules import FileProperty, Operator, LogicOperator, ActionType, Condition, Action, Rule

class TestCondition(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and test files for evaluation
        self.test_dir = "temp_test_dir"
        os.makedirs(self.test_dir, exist_ok=True)
        self.file1_path = os.path.join(self.test_dir, "document.pdf")
        self.file2_path = os.path.join(self.test_dir, "image_001.jpg")
        self.file3_path = os.path.join(self.test_dir, "report_final.docx")

        with open(self.file1_path, "w") as f:
            f.write("This is a PDF document.")
        with open(self.file2_path, "w") as f:
            f.write("This is a JPG image.")
        with open(self.file3_path, "w") as f:
            f.write("This is a DOCX report.")

        # Set modification times for testing IsOlderThan/IsNewerThan
        # Make file1 older
        old_time = datetime.now() - timedelta(days=30)
        os.utime(self.file1_path, (old_time.timestamp(), old_time.timestamp()))

    def tearDown(self):
        # Clean up the temporary directory and files
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_file_name_contains(self):
        condition = Condition(FileProperty.FileName, Operator.Contains, "docu")
        self.assertTrue(condition.evaluate(self.file1_path))
        self.assertFalse(condition.evaluate(self.file2_path))

    def test_file_extension_equals(self):
        condition = Condition(FileProperty.FileExtension, Operator.Equals, "pdf")
        self.assertTrue(condition.evaluate(self.file1_path))
        self.assertFalse(condition.evaluate(self.file2_path))

    def test_file_size_greater_than(self):
        # file1_path has ~24 bytes
        condition = Condition(FileProperty.FileSize, Operator.GreaterThan, 10)
        self.assertTrue(condition.evaluate(self.file1_path))
        condition = Condition(FileProperty.FileSize, Operator.GreaterThan, 100)
        self.assertFalse(condition.evaluate(self.file1_path))

    def test_last_modified_date_is_older_than(self):
        # file1 is 30 days old. Test if older than 15 days.
        condition = Condition(FileProperty.LastModifiedDate, Operator.IsOlderThan, timedelta(days=15))
        self.assertTrue(condition.evaluate(self.file1_path))
        # Test if older than 45 days.
        condition = Condition(FileProperty.LastModifiedDate, Operator.IsOlderThan, timedelta(days=45))
        self.assertFalse(condition.evaluate(self.file1_path))
        # file2 is recent, should not be older than 15 days
        condition = Condition(FileProperty.LastModifiedDate, Operator.IsOlderThan, timedelta(days=15))
        self.assertFalse(condition.evaluate(self.file2_path))

    def test_last_modified_date_is_newer_than(self):
        # file1 is 30 days old. Test if newer than 15 days. (Should be false)
        condition = Condition(FileProperty.LastModifiedDate, Operator.IsNewerThan, timedelta(days=15))
        self.assertFalse(condition.evaluate(self.file1_path))
        # file2 is recent, should be newer than 15 days
        condition = Condition(FileProperty.LastModifiedDate, Operator.IsNewerThan, timedelta(days=15))
        self.assertTrue(condition.evaluate(self.file2_path))

    def test_file_name_starts_with(self):
        condition = Condition(FileProperty.FileName, Operator.StartsWith, "docu")
        self.assertTrue(condition.evaluate(self.file1_path))
        condition = Condition(FileProperty.FileName, Operator.StartsWith, "imag")
        self.assertTrue(condition.evaluate(self.file2_path))

    def test_file_name_ends_with(self):
        condition = Condition(FileProperty.FileName, Operator.EndsWith, "ment")
        self.assertTrue(condition.evaluate(self.file1_path))
        condition = Condition(FileProperty.FileName, Operator.EndsWith, "final")
        self.assertFalse(condition.evaluate(self.file1_path))

    def test_file_name_matches_regex(self):
        condition = Condition(FileProperty.FileName, Operator.MatchesRegex, r"image_\d+")
        self.assertFalse(condition.evaluate(self.file1_path))
        self.assertTrue(condition.evaluate(self.file2_path))


class TestRule(unittest.TestCase):
    def setUp(self):
        self.test_dir = "temp_test_dir_rule"
        os.makedirs(self.test_dir, exist_ok=True)
        self.file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(self.file_path, "w") as f:
            f.write("Some content.")

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_rule_evaluate_and_logic(self):
        cond1 = Condition(FileProperty.FileName, Operator.Contains, "test")
        cond2 = Condition(FileProperty.FileExtension, Operator.Equals, "txt")
        rule = Rule("Test Rule AND", [cond1, cond2], LogicOperator.AND)
        self.assertTrue(rule.evaluate(self.file_path))

        cond3 = Condition(FileProperty.FileExtension, Operator.Equals, "pdf")
        rule_false = Rule("Test Rule AND False", [cond1, cond3], LogicOperator.AND)
        self.assertFalse(rule_false.evaluate(self.file_path))

    def test_rule_evaluate_or_logic(self):
        cond1 = Condition(FileProperty.FileName, Operator.Contains, "nonexistent")
        cond2 = Condition(FileProperty.FileExtension, Operator.Equals, "txt")
        rule = Rule("Test Rule OR", [cond1, cond2], LogicOperator.OR)
        self.assertTrue(rule.evaluate(self.file_path))

        cond3 = Condition(FileProperty.FileName, Operator.Contains, "nonexistent")
        cond4 = Condition(FileProperty.FileExtension, Operator.Equals, "pdf")
        rule_false = Rule("Test Rule OR False", [cond3, cond4], LogicOperator.OR)
        self.assertFalse(rule_false.evaluate(self.file_path))

    def test_rule_evaluate_no_conditions(self):
        rule = Rule("Unconditional Rule", [])
        self.assertTrue(rule.evaluate(self.file_path)) # Should be true

    def test_rule_evaluate_disabled(self):
        cond1 = Condition(FileProperty.FileName, Operator.Contains, "test")
        rule = Rule("Disabled Rule", [cond1], enabled=False)
        self.assertFalse(rule.evaluate(self.file_path))


class TestAction(unittest.TestCase):
    def setUp(self):
        self.base_dir = "temp_action_test_dir"
        self.src_dir = os.path.join(self.base_dir, "src")
        self.dest_dir = os.path.join(self.base_dir, "dest")
        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.dest_dir, exist_ok=True)

        self.test_file_name = "original_file.txt"
        self.test_file_path = os.path.join(self.src_dir, self.test_file_name)
        with open(self.test_file_path, "w") as f:
            f.write("Action test content.")
        
        self.placeholders = {
            "original_name": "original_file",
            "extension": "txt",
            "YYYY": "2026", "MM": "01", "DD": "23",
            "HH": "10", "MI": "30", "SS": "00",
        }


    def tearDown(self):
        if os.path.exists(self.base_dir):
            shutil.rmtree(self.base_dir)

    def test_move_action(self):
        new_path = os.path.join(self.dest_dir, self.test_file_name)
        action = Action(ActionType.Move, destination=new_path)
        self.assertTrue(action.execute(self.test_file_path, self.placeholders))
        self.assertTrue(os.path.exists(new_path))
        self.assertFalse(os.path.exists(self.test_file_path))

    def test_move_action_with_placeholder(self):
        # Move to dest/2026/01/original_file.txt
        new_dest_template = os.path.join(self.dest_dir, "{YYYY}", "{MM}", "{original_name}.{extension}")
        action = Action(ActionType.Move, destination=new_dest_template)
        
        expected_dest_path = os.path.join(self.dest_dir, "2026", "01", "original_file.txt")
        
        self.assertTrue(action.execute(self.test_file_path, self.placeholders))
        self.assertTrue(os.path.exists(expected_dest_path))
        self.assertFalse(os.path.exists(self.test_file_path))

    def test_rename_action(self):
        new_name = "renamed_file.txt"
        action = Action(ActionType.Rename, pattern=new_name)
        self.assertTrue(action.execute(self.test_file_path, self.placeholders))
        self.assertTrue(os.path.exists(os.path.join(self.src_dir, new_name)))
        self.assertFalse(os.path.exists(self.test_file_path))

    def test_rename_action_with_placeholder(self):
        # Rename to original_file_20260123.txt
        new_pattern = "{original_name}_{YYYY}{MM}{DD}.{extension}"
        action = Action(ActionType.Rename, pattern=new_pattern)

        expected_new_name = "original_file_20260123.txt"
        expected_new_path = os.path.join(self.src_dir, expected_new_name)

        self.assertTrue(action.execute(self.test_file_path, self.placeholders))
        self.assertTrue(os.path.exists(expected_new_path))
        self.assertFalse(os.path.exists(self.test_file_path))


if __name__ == '__main__':
    unittest.main()
