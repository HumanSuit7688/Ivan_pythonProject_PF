import sqlite3 as sl
con = sl.connect('my-test.db')

# with con:
#     con.execute("""
#         ADD COLUMN INTO USERS
#     """)

# sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
# data = [
#     (1, 'Alice', 21),
#     (2, 'Bob', 22),
#     (3, 'Chris', 23)
# ]



# with con:
#     con.executemany(sql, data)

sql = 'DELET USER'
