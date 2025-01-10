import sqlite3 as sq

with sq.connect("not_telegram.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE Users")
    cur.execute("""CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        )""")
    for num in range(1, 11):
        cur.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)", (f"User{num}", f"example{num}@gmail.com", f"{num*10}", "1000"))

    for num in range(1, 11, 2):
        cur.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f'{num}'))

    for num in range(1, 11, 3):
        cur.execute("DELETE FROM Users WHERE id = ?", (f'{num}',))

    cur.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
    users = cur.fetchall()
    for user in users:
        print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')