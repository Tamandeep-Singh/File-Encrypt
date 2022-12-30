# -----------------------------------------------------------
# filename: test_file_utils.py
#
# Description: Unit test for file utils.
# Github Repo: https://github.com/Tamandeep-Singh/File-Encrypt
# Released under MIT License 
# -----------------------------------------------------------

import unittest
import json
import sys
sys.path.insert(0, '/home/tam/Projects/File-Encrypt/lib')
import file_utils as FileUtils

class TestFileUtils(unittest.TestCase):

    def test_does_file_exist(self):
       """Check if does_file_exist returns the correct boolean."""
       self.assertTrue(FileUtils.does_file_exist("../README.md"))
       self.assertTrue(FileUtils.does_file_exist("../test.txt"))
       self.assertFalse(FileUtils.does_file_exist("testfile.txt"))
       self.assertFalse(FileUtils.does_file_exist("randomfile.csv"))

    def test_get_file_data(self):
        """Test if file data is successfully extracted and that None is returned if file doesn't exist."""
        test_file_data = "MOCK_DATA, 123456789, ABCDEF, IGNORE"
        self.assertEqual(FileUtils.get_file_data("test_file.txt", "r"), test_file_data)
        self.assertIsNone(FileUtils.get_file_data("randomfile.csv", "r"))
    
    def test_get_file_without_ext(self):
        """Test that the filename is returned without the extension."""
        self.assertEqual(FileUtils.get_file_without_ext("test.txt"), "test")
        self.assertEqual(FileUtils.get_file_without_ext("random_file.csv"), "random_file")
        self.assertEqual(FileUtils.get_file_without_ext("logger.test.py"), "logger.test")


    def test_write_to_file(self):
        """Test if a file can be created with the correct data."""
        test_data = "This is some mock data to test if the data can be written to a file"
        FileUtils.write_to_file("test_write_file.txt", test_data, "w")
        self.assertTrue(FileUtils.does_file_exist("test_write_file.txt"))
        self.assertEqual(FileUtils.get_file_data("test_write_file.txt", "r"), test_data)

    def test_write_to_file_json(self):
        """Test if a file can be created and store the correct JSON data."""
        test_data = {
            'day':'Friday',
            'date':'30',
            'year':2022,
            'purpose':'mock_test_data'
        }
        FileUtils.write_to_file_json("test_write_file.json", test_data, "w")
        self.assertTrue(FileUtils.does_file_exist("test_write_file.json"))
        self.assertEqual(json.loads(FileUtils.get_file_data("test_write_file.json", "r")), test_data)



if __name__ == "__main__":
    """Run main unittest for testing FileUtils."""
    unittest.main()