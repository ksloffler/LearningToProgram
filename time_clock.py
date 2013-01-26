from datetime import datetime
import sqlite3

class TimeClock:
    def __init__(self):
        self.db_connection = sqlite3.connect('time_clock_db')
        self.db_connection.row_factory = sqlite3.Row
        self.db = self.db_connection.cursor()
        self.create_db_if_not_exists()

    def create_db_if_not_exists(self):
        self.db.execute(''.join(['CREATE TABLE IF NOT EXISTS `times`',
                                     '(id INTEGER PRIMARY KEY AUTOINCREMENT, ',
                                     'time_in DATETIME, time_out DATETIME)']))

    def insert(self, table, columns_and_values):
        columns = []
        values = []
        for key, value in columns_and_values.items():
            columns.append(''.join(["'", str(key), "'"]))
            values.append(''.join(["'", str(value), "'"]))

        columns = ', '.join(columns)
        values = ', '.join(values)

        print('INSERT INTO `%s`(%s) VALUES (%s)' % (table, columns, values))
        self.db.execute('INSERT INTO `%s`(%s) VALUES (%s)' % (table, columns, values))
        self.db_connection.commit()
        
    def execsql(self, statement, fetchall=True):
        result = self.db.execute(statement).fetchall()
        self.db_connection.commit()

        return result if fetchall else result[0]

    def records_between(self, start_date, end_date):
        records = self.execsql("""SELECT `time_in`, `time_out`
                                  FROM `times`
                                  WHERE `time_in` BETWEEN '%s'
                                                      AND '%s'""" % (
                                  start_date, end_date))
        return records

tc = TimeClock()

tc.execsql('DELETE FROM `times`')
tc.insert('times', {'time_in':datetime.now(),
                    'time_out':datetime.now()
                    })

tc.insert('times', {'time_in':datetime(2011, 1,2, 8),
                    'time_out':datetime(2011, 1, 2, 10)
                   })

#print(tc.execsql('SELECT `time_in`, `time_out` FROM `times`'))

print(tc.records_between('2011-01-01', '2011-01-03')[0]['time_in'])
    
