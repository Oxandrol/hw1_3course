import sqlite3
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("mentor.sqlite3")
    cursor = db.cursor()

    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors"
        "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "username VARCHAR (30),"
        "name VARCHAR(20),"
        "direction VARCHAR(20),"
        "age INTEGER,"
        "groupe VARCHAR(10))"
    )

    db.execute(
        "CREATE TABLE IF NOT EXISTS users "
        "(id INTEGER PRIMARY KEY, "
        "username VARCHAR(50),"
        "name VARCHAR (50)) "
    )

    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO anketa VALUES "
            "(null, ?, ?, ?, ?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()


async def sql_command_all_users():
    return cursor.execute("SELECT * FROM users").fetchall()


async def sql_command_insert_user(id, username, name):
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (id, username, name))
    db.commit()


async def sql_command_insert_new(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO mentors VALUES "
            "(null, ?, ?, ?, ?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()


async def sql_command_random():
    users = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(users)
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (id,))
    db.commit()
