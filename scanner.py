import sqlite3
import dbworker
import csv
import datetime

escuela = input("Escuela: ")
conn = sqlite3.connect(f'{escuela}.db')
c = conn.cursor()

print(datetime.time.hour)
# while True:
#     dbworker.studentSearch(c)
#cambio que hice pa ver la cosa de github funcionar