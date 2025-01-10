import sqlite3 as sq

with sq.connect("not_telegram.db") as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE Users")
    cur.execute("DELETE FROM Users WHERE id = ?", (6,))
    cur.execute("SELECT COUNT(*) FROM Users" )
    total_users = cur.fetchone()[0]
    cur.execute("SELECT SUM(balance) FROM Users ")
    all_balances = cur.fetchone()[0]
    print(all_balances/total_users)