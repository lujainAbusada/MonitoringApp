import unittest
from unittest import mock
import sys
sys.path.insert(0, '/MonitoringApp/Application')
import Statistics
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class Test_insert_rows(unittest.TestCase):

    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc

    def test_insert_rows_calls_executemany_and_commit_passing_correct_arguments(self):     
        
        dbc = self.fix_dbc()
        Statistics.CPU_Usage(dbc)
        with dbc.cursor() as cursor:
            expect_sql = "INSERT INTO CPU(Utilization,time) VALUES(%s,%s)"
            CPU_data = (1,current_time)
            calls = [mock.call.execute(expect_sql, CPU_data),
                 mock.call.commit(),]
            cursor.assert_has_calls(calls)
            self.assertTrue(dbc.autocommit)

if __name__ == '__main__':
    unittest.main(argv=['', '-v'])
