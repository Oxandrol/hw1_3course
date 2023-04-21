import sqlite3
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("mentor.sqlite3")
    cursor = db.cursor()

    db.execute(
        "CREATE TABLE IF NOT EXISTS mentors"
        "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name VARCHAR(20),"
        "direction VARCHAR(20),"
        "age INTEGER,"
        "groupe VARCHAR(10))"
    )
    db.commit()


async def sql_command_insert(state):
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


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()


sql_create()
