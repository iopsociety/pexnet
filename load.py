def load_data():
    import sqlite3
    conn = sqlite3.connect('pexnet.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE tasks (id integer primary key, task text, desirability_rating real, empowerment_rating real)''')
    i = 1
    for t in open('textfiles/tasks.txt'):
         c.execute("""INSERT INTO tasks VALUES (%d, "%s", 2, 2)""" % (i, t[:-1].replace("'", "\'")))
         i = i + 1
    i = 1
    c.execute('''CREATE TABLE goods (id integer primary key, good text, description text, price real)''')
    for g in open('textfiles/goods.txt'):
         f = g[:-1].replace("'", "\'").split(':')
         c.execute("""INSERT INTO goods VALUES (%d, "%s", "%s", 5)""" % (i, f[0].strip(), f[1].strip()))
         i = i + 1
    c.execute('''CREATE TABLE my_goods (id integer primary key, good_id id, quantity real)''')
    c.execute('''CREATE TABLE my_tasks (id integer primary key, task_id id, hours real)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_data()
