import sqlite3 

# открываем файл с базой данных
con = sqlite3.connect('shoplist.db')

# создаём таблицу 
# with con:
#     con.execute("""
#         CREATE TABLE shopping (
#             ID INTEGER PRIMARY KEY,
#             name TEXT,
#             type TEXT,
#             date TEXT,
#             price INTEGER
# );
#     """)
# data = [
#     (1, 'fan', 'model_3', '2023', 150),
#     (2, 'computer', 'ausk3x', '2025', 2500)
# ]
# with con:
#     con.executemany("""INSERT INTO shopping (ID, name, type, date, price) values(?, ?, ?, ?, ?)""", data)
# with con:
#     con.execute(""" UPDATE shopping SET price = ? WHERE name = ? """, (200, 'fan'))

with con:
    con.execute(""" DELETE FROM shopping WHERE name = ? """, ('computer',))