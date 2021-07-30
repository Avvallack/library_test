"""
Tests module for package
"""

import os.path
import unittest
import pandas as pd
from get_data.get_data import get_hour_data


class TestGetDataMethods(unittest.TestCase):
    """
    Test cases for get_data module
    """
    def test_basic_path(self):
        """
        tests path creation
        :return: None
        """
        get_hour_data('AAPL', '2020-08-01-13')
        self.assertTrue(os.path.isdir('./data/original'))

    def test_file_creation(self):
        """
        tests file creation
        :return: None
        """
        get_hour_data('AAPL', '2020-09-01-14')
        self.assertTrue(os.path.isfile('./data/original/AAPL/2020-09-01/13.csv'))

    def test_file_columns(self):
        """
        tests dataframe shape
        :return: None
        """
        get_hour_data('AAPL', '2020-10-01-15')
        sample_df = pd.read_csv('./data/original/AAPL/2020-10-01/14.csv')
        self.assertEqual((60, 8), sample_df.shape)


if __name__ == '__main__':
    unittest.main()
