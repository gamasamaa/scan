import sqlite3

def printp(printable):
    print(">>>", printable)

def studentTableCreate():
    exist = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = 'estudiantes'")
    temp = exist.fetchall()
    if len(temp) == 0:
        cursor.execute("create table estudiantes(id, nombre, grado, categoria)")
        print("base de datos creadas")
    else:
        print("base de datos ya existe")

def studentEntry():
    idt = input("ID del estudiante: ")
    if idt == "":
        return False
    nombret = input("Nombre completo del estudiante: ")
    gradot = input("Grado del estudiante: ")
    categoriat = input("Categoria del estudiante: ")
    q = cursor.execute(f'INSERT OR IGNORE INTO estudiantes VALUES("{idt}", "{nombret}","{gradot}","{categoriat}")')
    printp("Entraste " + nombret + " " + gradot + " " + categoriat)
    return True

def studentSearch():
    temp = input("Que estudiante busca?")
    q = cursor.execute(f'SELECT * FROM estudiantes WHERE nombre = "{temp}"' )
    q1 = q.fetchone()
    print(q1)

def studentDelete():
    target = input("Que estudiante quieres borrar: ")
    cursor.execute(f'DELETE FROM estudiantes WHERE nombre = "{target}"')
    
def studentDelete():
    target = input("Que estudiante quieres borrar: ")
    cursor.execute(f'DELETE FROM estudiantes WHERE nombre = "{target}"')
    if cursor.execute(f'SELECT * FROM estudiantes WHERE nombre = "{target}"') == None:
        print("Borraste a " + target + "exitosamente")
    else:
        print("me pingue :P")

school = input("Que escuela vas a trabajar: ")

c = sqlite3.connect(f'{school}.db')
print(c)
cursor = c.cursor()

# data = [
#     (1, "Sofía Mendoza", 12, 1),
#     (2, "Andrea Mendoza", 9, 1),
#     (3, "Alejandro Reyes", 12, 2),
#     (4, "Carlos Rodriguez", 6, 3),
# ]



while True:
    
    coso = input(">>> Que quieres hacer? \n\n Crear una base de datos, Buscar, Entrar un estudiante, Entrar mutiples estudiantes, Entrar multiples estudiantes desde un file, Borrar, Cerrar\n\n>>> ")
    
    match coso:
        case "Crear una base de datos":
            studentTableCreate()
        case "Buscar":
            studentSearch()
        case "Entrar":
            studentEntry()
        case "Entrar multiples estudiantes":
            while studentEntry():
                print("fue añadido a la base de datos")
        case "Entrar multiples estudiantes desde un file":
            file = input("Nombre del file: ")
            print(f'Estudiantes añadidos de {file}')
        case "Borrar":
            studentDelete()
        case "Cerrar":
            print("\nAdios my guy\n\nCerrar\n")
            break
        case _:
            print("\nQue?\n")
    c.commit()