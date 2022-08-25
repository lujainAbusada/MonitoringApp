import unittest
from unittest import mock
import sys
sys.path.insert(0, '/MonitoringApp/Application')
from StoreStatistics import StoreUsage


class Test_StoreUsage(unittest.TestCase):

    def test_StoreUsage_Disk(self):
        dbc = mock.MagicMock(name="dbconn")
        values = ("1","1","1","1")
        query = "INSERT INTO Disk(used,total,free,time) VALUES(%s,%s,%s,%s)"
        StoreUsage(dbc,values, query, 'Disk', 23)
        self.assertTrue(dbc.cursor.called)
        self.assertTrue(dbc.cursor().execute.called)
        self.assertTrue(dbc.commit.called)

if __name__ == '__main__':
    unittest.main(argv=['', '-v'])

