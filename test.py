import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

user = (1, 'souvik', '123456')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)


users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]

cursor.executemant(insert_query, users)

# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)

connection.commit()

connection.close()
