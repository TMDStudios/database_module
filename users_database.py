import sqlite3

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username text,
    password text,
    email text
)"""
ADD_USER = "INSERT INTO users VALUES (?, ?, ?)"
GET_USERS = "SELECT * FROM users"


def connect():
    return sqlite3.connect('users.db')


def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)


def add_user(connection, username, password, email):
    with connection:
        connection.execute(ADD_USER, (username, password, email))


def get_users(connection):
    with connection:
        users = []
        for i in connection.execute(GET_USERS).fetchall():
            users.append(i[0])
        print(users)
        return users


def close_connection(connection):
    connection.close()
