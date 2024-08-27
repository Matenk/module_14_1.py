import sqlite3
from pprint import pprint

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")


# for i in range(1, 11):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', i*10, '1000'))

# cursor.execute("UPDATE Users SET balance = ? WHERE id % 2!=0", (500, ))

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

for num_user in range(1, len(users) + 1, 3):
   cursor.execute("DELETE FROM Users WHERE id = ?", (num_user,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60, ))
users = cursor.fetchall()
for user in users:
    username, email, age, balance = user
    print(f'Имя: {username}| Почта: {email}| Возраст: {age}| Баланс: {balance}')










connection.commit()
connection.close()
