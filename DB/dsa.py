import sqlite3 as sl
con = sl.connect('my-test.db')

# with con:
#     con.execute("""
#         CREATE TABLE USER (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             age INTEGER
#         );
#     """)

# sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
# data = [
#     (1, 'Alice', 21),
#     (2, 'Bob', 22),
#     (3, 'Chris', 23)
# ]



# with con:
#     con.executemany(sql, data)
names = []
with con:
    data = con.execute("SELECT name FROM USER")
    print(data)
    for row in data:
        names += row
print(names)

def log_up(nickname):
    if nickname in names:
        x = 1
