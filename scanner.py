import sqlite3
import dbworker
import csv
import datetime

escuela = input("Escuela: ")
conn = sqlite3.connect(f'{escuela}.db')
c = conn.cursor()

print(datetime.datetime.now())
# while True:
#     dbworker.studentSearch(c)