import sqlite3
import dummy
import csv
import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

escuela = input("Escuela: ")
conn = sqlite3.connect(f'{escuela}.db')
c = conn.cursor()

print(datetime.datetime.now())
app = QApplication(sys.argv)
window = QMainWindow()
window.show()
app.exec()
while True:
    dummy.studentSearch()
    lista = c.execute("select * from estudiantes")
    print(lista.fetchall())