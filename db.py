import sqlite3 as sl
con = sl.connect('my-test.db')

with con:
    con.execute("""
        CREATE TABLE users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            click_count INTEGER
        );
    """)
# sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
# data = [
#     (1, 'Alice', 21),
#     (2, 'Bob', 22),
#     (3, 'Chris', 23)
# ]



# with con:
#     con.executemany(sql, data)'
