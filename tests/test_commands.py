import unittest
import os
import shutil
import json
from src.commands import list, save_txt, read_txt, save_json, load_json, create_directory

# Written automatically by Gemini, might not work 100%
class TestCommands(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_dir"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory
        shutil.rmtree(self.test_dir)

    def test_list(self):
        # Create some test folders
        os.makedirs(os.path.join(self.test_dir, "folder1"))
        os.makedirs(os.path.join(self.test_dir, "folder2"))

        # Test listing folders
        folders = list(self.test_dir)
        self.assertIn("folder1", folders)
        self.assertIn("folder2", folders)

        # Test listing non-existent directory
        non_existent_dir = os.path.join(self.test_dir, "non_existent")
        folders = list(non_existent_dir)
        self.assertEqual(folders, [])

    def test_save_txt(self):
        # Test saving text to a file
        file_name = os.path.join(self.test_dir, "test.txt")
        content = "This is a test string."
        save_txt(file_name, content)

        # Verify the content of the file
        with open(file_name, 'r') as f:
            self.assertEqual(f.read(), content)

    def test_read_txt(self):
        # Create a test file
        file_name = os.path.join(self.test_dir, "test.txt")
        with open(file_name, 'w') as f:
            f.write("Test content")

        # Test reading the file
        content = read_txt(file_name)
        self.assertEqual(content, "Test content")

        # Test reading a non-existent file
        non_existent_file = os.path.join(self.test_dir, "non_existent.txt")
        content = read_txt(non_existent_file)
        self.assertEqual(content, '')

    def test_save_json(self):
        # Test saving JSON data to a file
        file_name = os.path.join(self.test_dir, "test.json")
        data = {"key1": "value1", "key2": 2}
        save_json(file_name, data)

        # Verify the content of the file
        with open(file_name, 'r') as f:
            loaded_data = json.load(f)
            self.assertEqual(loaded_data, data)

    def test_load_json(self):
        # Create a test JSON file
        file_name = os.path.join(self.test_dir, "test.json")
        with open(file_name, 'w') as f:
            json.dump({"key1": "value1", "key2": 2}, f)

        # Test loading JSON data from a file
        loaded_data = load_json(file_name)
        self.assertEqual(loaded_data, {"key1": "value1", "key2": 2})

        # Test loading a non-existent file
        non_existent_file = os.path.join(self.test_dir, "non_existent.json")
        loaded_data = load_json(non_existent_file)
        self.assertIsNone(loaded_data)

        # Test loading an invalid JSON file
        invalid_json_file = os.path.join(self.test_dir, "invalid.json")
        with open(invalid_json_file, 'w') as f:
            f.write("This is not valid JSON")
        loaded_data = load_json(invalid_json_file)
        self.assertIsNone(loaded_data)

    def test_create_directory(self):
        # Test creating a new directory
        directory = os.path.join(self.test_dir, "new_dir")
        create_directory(directory)
        self.assertTrue(os.path.exists(directory))

        # Test creating an existing directory
        create_directory(directory)
        self.assertTrue(os.path.exists(directory))

if __name__ == '__main__':
    unittest.main()
