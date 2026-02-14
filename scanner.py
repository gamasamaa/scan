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
# otro cambio a lo loco pa ver como brega
# hacer cambios aca para bregar con el pull
# vamos a ver mas cambios webo webo webo