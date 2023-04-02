import sqlite3
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS countries
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL)''')

cursor.execute("INSERT INTO countries (title) VALUES ('Россия'), "
               "('США'),"
               " ('Китай')")

cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   area REAL DEFAULT 0,
                   country_id INTEGER NOT NULL,
                   FOREIGN KEY(country_id) REFERENCES countries(id))''')

cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Москва', 1),"
               " ('Нью-Йорк', 2),"
               " ('Шанхай', 3),"
               " ('Пекин', 3),"
               " ('Токио', 4),"
               " ('Париж', 5), "
               "('Берлин', 6)")



cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   city_id INTEGER NOT NULL,
                   FOREIGN KEY(city_id) REFERENCES cities(id))''')

cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Сергей', 'Иванов', 1),"
               " ('Петр', 'Петров', 2),"
               " ('Анна', 'Ахматова', 3),"
               " ('Ирина', 'Шайгу', 3),"
               " ('Константин', 'Хабенский', 7),"
               " ('Александр', 'Сергеев', 5),"
               " ('Ольга', 'Картункова', 6),"
               " ('Алексей', 'Учитель', 6),"
               " ('Аполинария', 'Еленова', 4),"
               " ('Артур', 'Рахманов', 7),"
               " ('Мария', 'Кравец', 4),"
               " ('Дмитрий', 'Лысый', 3),"
               " ('Наталья', 'Спасокукоцкая', 2),"
               " ('Александр', 'Пушкин', 7),"
               " ('Екатерина', 'Вторая', 5)")

conn.commit()



cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()
print("Список городов:")
for city in cities:
    print(str(city[0]) + " - " + city[1])

city_id = int(input("Введите id города для вывода списка сотрудников или 0 для выхода: "))

while city_id != 0:
    cursor.execute('''SELECT employees.first_name, employees.last_name, countries.title, cities.title
                          FROM employees
                          JOIN cities ON employees.city_id = cities.id
                          JOIN countries ON cities.country_id = countries.id
                          WHERE cities.id = ?''', (city_id,))
    employees = cursor.fetchall()
    print("Сотрудники в городе:")
    for employee in employees:
        print(employee[0] + " " + employee[1] + " - " + employee[2] + ", " + employee[3])

    city_id = int(input(f"Введите id города ({city}) для вывода списка сотрудников или 0 для выхода: "))

conn.close()