import os.path
import unittest
from get_data.get_data import get_hour_data
import pandas as pd


class TestGetDataMethods(unittest.TestCase):

    def test_basic_path(self):
        get_hour_data('AAPL', '2020-08-01-13')
        self.assertTrue(os.path.isdir('./data/original'))

    def test_file_creation(self):
        get_hour_data('AAPL', '2020-09-01-14')
        self.assertTrue(os.path.isfile('./data/original/AAPL/2020-09-01/13.csv'))

    def test_file_columns(self):
        get_hour_data('AAPL', '2020-10-01-15')
        df = pd.read_csv('./data/original/AAPL/2020-10-01/14.csv')
        self.assertEqual((60, 8), df.shape)


if __name__ == '__main__':
    unittest.main()
