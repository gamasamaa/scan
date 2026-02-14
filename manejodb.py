import sqlite3

escuela = input("Escuela: ")
conn = sqlite3.connect('big.db')
cursor = conn.cursor()
cursor.execute("create table if not exists escueladisponibles(escuelas unique)")
q = f"insert or ignore into escueladisponibles values('{escuela}')"
print(q)
cursor.execute(q)
conn.commit()
cursor.execute("select escuelas from escueladisponibles")
print(cursor.fetchall())
conn.close()