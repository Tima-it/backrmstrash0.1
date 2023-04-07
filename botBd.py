import sqlite3 as sq

with sq.connect("backroomsBot.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS backroomslvl(
     name TEXT,
     description TEXT,
     photo BLOB
    ) """)
    con.commit()
    backroomsLvlBd = cur.execute("SELECT * FROM `backroomslvl`")
    resultlvl = cur.fetchall()
    


with sq.connect("backroomsBot.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS backroomsitem(
     name TEXT,
     description TEXT,
     photo BLOB
    ) """)
    con.commit()
    backroomsItemBd = cur.execute("SELECT * FROM `backroomsitem`")


with sq.connect("backroomsBot.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS backroomsteam(
     name TEXT,
     description TEXT
    ) """)
    con.commit()
    backroomsteamBd = cur.execute("SELECT * FROM `backroomsteam`")


with sq.connect("backroomsBot.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS backroomsmonster(
     name TEXT,
     description TEXT,
     photo BLOB
    ) """)
    con.commit()
    backroomsmonsterBd = cur.execute("SELECT * FROM `backroomsmonster`")
