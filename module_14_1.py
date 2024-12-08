import sqlite3

# Создаем БД not_telegram.db
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Удаляем таблицу Users, если она существует. Для того, чтобы таблица не разрасталась в случае
# нескольких запусков срипта подряд в процессе написания.
cursor.execute("DROP TABLE IF EXISTS Users")

# Создаем таблицу Users в БД not_telegram.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# Заполняем таблицу Users 10-ю записями согласно условию
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', i*10, 1000))

# Обновляем balance у каждой 2-ой записи начиная с 1-ой на 500
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",
                   (500, i))

# Удаляем каждую 3-ю запись в таблице начиная с 1-ой
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?",
                   (i,))

# Получаем все записи, где возраст не равен 60
cursor.execute("SELECT * FROM Users WHERE age <> ?",
               (60,))
users = cursor.fetchall()

# Выводим полученные записи в консоль в заданном формате
for row in users:
    print(f"Имя:{row[1]} | Почта:{row[2]} | Возраст:{row[3]} | Баланс:{row[4]}")

connection.commit()
connection.close()
