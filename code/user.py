import sqlite3

class User:
    """docstring for User."""
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()

        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else
            user = None

        connection.close()
        return user
