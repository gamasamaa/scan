import sqlite3
import csv
from PyQt6.QtWidgets import QApplication, QWidget
import sys

def printp(printable):
    print(">>>", printable)

def studentTableCreate():
    cursor.execute("create table if not exists estudiantes(id, nombre, grado, categoria)")

def studentEntry():
    idt = input("ID del estudiante: ")
    while len(idt) <= 0:
        print("tienes que darme un id")
        idt = input("ID del estudiante: ")

    nombret = input("Nombre completo del estudiante: ")
    while len(nombret) <= 0:
        print("tienes que darme un nombre")
        nombret = input("nombre del estudiante: ")

    gradot = input("Grado del estudiante: ")
    while len(gradot) <= 0:
        print("tienes que darme un grado")
        gradot = input("grado de estudiante:")

    categoriat = input("Categoria del estudiante: ")
    while len(categoriat) <= 0:
        print("tienes que darme una categoria")
        categoriat = input("categoria:")

    q = cursor.execute("insert or ignore into estudiantes values(?,?,?,?)", (idt, nombret, gradot, categoriat))
    printp("Entraste " + nombret + " " + gradot + " " + categoriat)
    return True

def studentSearch():
    temp = input("Que estudiante busca?")
    q = cursor.execute("select * from estudiantes where nombre = ?", [temp])
    q1 = q.fetchone()
    print(q1)

def studentDelete():
    target = input("Que estudiante quieres borrar: ")
    cursor.execute("delete from estudiantes where nombre = ?", [target])
    
def studentDelete():
    target = input("Que estudiante quieres borrar: ")
    cursor.execute("delete from estudiantes where nombre = ?", [target])
    result = cursor.execute("select * from estudiantes where nombre = ?", [target])
    if result.fetchall() == []:
        print("Borraste a " + target + " exitosamente")
    else:
        print("me pingue :P")

school = input("Que escuela vas a trabajar: ")

c = sqlite3.connect(f"{school}.db")
print(c)
cursor = c.cursor()

# data = [
#     (1, "Sofía Mendoza", 12, 1),
#     (2, "Andrea Mendoza", 9, 1),
#     (3, "Alejandro Reyes", 12, 2),
#     (4, "Carlos Rodriguez", 6, 3),
# ]



# while True:
    
#     coso = input(">>> Que quieres hacer? \n\n Crear una base de datos, Buscar, Entrar un estudiante, Entrar mutiples estudiantes, Entrar multiples estudiantes desde un file, Borrar, Cerrar\n\n>>> ")
    
#     match coso:
#         case "Crear una base de datos":
#             studentTableCreate()
#         case "Buscar":
#             studentSearch()
#         case "Entrar":
#             studentEntry()
#         case "Entrar multiples estudiantes":
#             while studentEntry():
#                 print("fue añadido a la base de datos")
#         case "Entrar multiples estudiantes desde un file":
#             file = input("Nombre del file: ")
#             print(f'Estudiantes añadidos de {file}')
#         case "Borrar":
#             studentDelete()
#         case "Cerrar":
#             print("\nAdios my guy\n\nCerrar\n")
#             break
#         case _:
#             print("\nQue?\n")
#     c.commit()