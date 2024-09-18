# tests/test_data_loader.py
import unittest
from spatialdatasets import load
from pathlib import Path

class TestDataLoader(unittest.TestCase):
    def test_load(self):
        dataset_dir = load("tanksandtemple")
        self.assertTrue(dataset_dir.exists())
        self.assertTrue(any(dataset_dir.iterdir()))  # Check if files are extracted

if __name__ == "__main__":
    unittest.main()
