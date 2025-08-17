import sqlite3


with sqlite3.connect('todo.db') as connection:
    cursor = connection.cursor()
    connection.execute("PRAGMA foreign_keys = ON;")
    cursor.executescript("""
CREATE TABLE IF NOT EXISTS users (
    uuid TEXT PRIMARY KEY,
    user_name TEXT NOT NULL,
    age TEXT,
    mail_address TEXT NOT NULL,
    created_at DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS todos (
    uuid TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    status BOOLEAN NOT NULL,
    start_date DATE NOT NULL,
    limit_date DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS user_todos (
    user_uuid TEXT NOT NULL,
    todo_uuid TEXT NOT NULL,
    FOREIGN KEY (user_uuid) REFERENCES users(uuid),
    FOREIGN KEY (todo_uuid) REFERENCES todos(uuid),
    PRIMARY KEY (user_uuid, todo_uuid)
);
    """)