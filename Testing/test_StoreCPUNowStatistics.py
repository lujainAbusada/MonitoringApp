import unittest
from unittest import mock
import sys
sys.path.insert(0, '/MonitoringApp/Application')
from StoreStatistics import StoreUsage


class Test_StoreUsage(unittest.TestCase):

    def test_StoreUsage_CPUNow(self):
        dbc = mock.MagicMock(name="dbconn")
        values = ("1","1")
        query = "INSERT INTO CPUNow(Utilization,time) VALUES(%s,%s)"
        StoreUsage(dbc,values, query, 'CPUNow', 100)
        self.assertTrue(dbc.cursor.called)
        self.assertTrue(dbc.cursor().execute.called)
        self.assertTrue(dbc.commit.called)

if __name__ == '__main__':
    unittest.main(argv=['', '-v'])

