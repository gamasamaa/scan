import sqlite3
import csv
from PyQt6.QtWidgets import QApplication, QWidget
import sys

def printp(printable):
    print(">>>", printable)

def studentTableCreate():
    cursor.execute("create table if not exists estudiantes(id unique not null, nombre unique not null, grado not null, categoria not null)")

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
    
def studentEntryCSV():
    file = input("Nombre del file: ")
    with open(file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            cursor.execute("insert or ignore into estudiantes values(?,?,?,?)", row)
    printp("Entraste " + file)

def studentSearch():
    temp = input("Que estudiante busca?")
    q = cursor.execute("select * from estudiantes where nombre = ?", [temp])
    q1 = q.fetchone()
    print(q1)

# def studentDelete():
#     target = input("Que estudiante quieres borrar: ")
#     cursor.execute("delete from estudiantes where nombre = ?", [target])
    
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
cursor = c.cursor()

# data = [
#     (1, "Sofía Mendoza", 12, 1),
#     (2, "Andrea Mendoza", 9, 1),
#     (3, "Alejandro Reyes", 12, 2),
#     (4, "Carlos Rodriguez", 6, 3),
# ]



while True:
    
    coso = input(">>> Que quieres hacer? \n\n Crear una base de datos, Buscar, Entrar un estudiante, Entrar mutiples estudiantes, Entrar multiples estudiantes desde un file, Borrar, Cerrar\n\n>>> ")
    coso = coso.lower()
    match coso:
        case "crear":
            studentTableCreate()
        case "buscar":
            studentSearch()
        case "entrar":
            studentEntry()
        case "entrarm":
            control = input("añadir estudiante?")
            while control != "no":
                studentEntry()
                control = input("añadir estudiante?")
        case "entrarmf":
            studentEntryCSV()
        case "borrar":
            studentDelete()
        case "cerrar":
            print("\nAdios my guy\n\nCerrar\n")
            break
        case "ver":
            temp = cursor.execute("select * from estudiantes")
            for i in temp:
                print(i[1], i[0], i[2])
        case _:
            print("\nQue?\n")
    c.commit()