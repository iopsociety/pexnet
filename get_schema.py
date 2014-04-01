import sqlite3
conn = sqlite3.connect('pexnet.db')
c = conn.cursor()
a = c.execute('''select * from sqlite_master''')
for i in a:
    print i
