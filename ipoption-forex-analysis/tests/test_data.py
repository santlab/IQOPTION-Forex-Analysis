import unittest
from src.data.loader import load_data
from src.data.providers import DataProvider

class TestDataLoading(unittest.TestCase):

    def setUp(self):
        self.provider = DataProvider()
        self.test_data_path = 'path/to/test/data.csv'  # Update with actual test data path

    def test_load_data(self):
        data = load_data(self.test_data_path)
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_data_provider(self):
        data = self.provider.get_data()
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()