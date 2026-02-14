import sqlite3

escuela = input("Escuela: ")
conn = sqlite3.connect('big.db')
cursor = conn.cursor()
cursor.execute("create table if not exists escueladisponibles(escuelas unique)")
cursor.execute("insert or ignore into escueladisponibles values(?)", [escuela])

cursor.execute("select escuelas from escueladisponibles")
print(cursor.fetchall())
while(True):
    c = input('que:')
    if c == 'x':
        break
    search = input("searching:")
    cursor.execute(f"select escuelas from escueladisponibles where escuelas = '{search}' ")
    if cursor.fetchall() == []:
        print("na que ver")
    else:
        print("found")
target = input("Borrar: ")
cursor.execute("delete from escueladisponibles where escuelas = ?", [target])
conn.commit()
conn.close()