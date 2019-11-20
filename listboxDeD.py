import sqlite3

#  USUARIOS

def buscar_u(buscar):
    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM usuarios """)
    a = cursor.fetchall()
    for z in a:
        buscar.insert(0,z)
    conn.commit()
    conn.close()

#   PERSONAGENS

def buscar_p(buscar):
    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM personagens """)
    a = cursor.fetchall()
    for z in a:
        buscar.insert(0,z[0] + '   |   ' + z[1] + '   |   ' + z[2] + '   |   ' + z[3] + '   |   ' + z[4] + '   |   ' + z[5])
    conn.commit()
    conn.close()

#  RAÇAS

def buscar_u(buscar):
    conn = sqlite3.connect("RacasDeD.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM racas """)
    a = cursor.fetchall()
    for z in a:
        buscar.insert(0,z)
    conn.commit()
    conn.close()
