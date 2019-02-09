import cx_Oracle
from copy import copy


username = input('enter username: ')
password = input('enter password: ')
host = input('enter host: ')
sid = input('enter SID: ')

conn = cx_Oracle.connect(username +'/' +password +'@' + host + '/' + sid)
cur = conn.cursor()

cur.execute('SELECT table_name FROM dba_tables')
tables = copy(cur)

for table in tables:
    print(table)
    cur.execute("select column_name from all_tab_columns where table_name = '{}'".format(table))
    table.columns = copy(cur)
    for column in table.columns:
        print("    " + column)

while True:
    query = input('enter your query: ')
    cur.execute(query)
    for line in cur:
        print(line)
    
