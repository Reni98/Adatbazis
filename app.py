import sqlite3
from pprint import pprint

# Adatbázis létrehozás
conn = sqlite3.connect("felhasznalo.db")
curs = conn.cursor()
#Tábla létrehozás
curs.execute("CREATE TABLE IF NOT EXISTS szemely (nev TEXT, kor INTEGER,nem TEXT)")
#Tábla feltöltése adatokkal
# curs.execute("INSERT INTO szemely VALUES ('John', 32, 'ferfi')")
# curs.execute("INSERT INTO szemely VALUES ('Erika', 42, 'no')")
# curs.execute("INSERT INTO szemely VALUES ('Kinga', 52, 'no')")
# curs.execute("INSERT INTO szemely VALUES ('Leonard', 51, 'ferfi')")
# curs.execute("INSERT INTO szemely VALUES ('Emily', 35, 'no')")
# curs.execute("INSERT INTO szemely VALUES ('Edward', 27, 'ferfi')")

#Az adatok megjelenítése a táblából
curs.execute("SELECT * FROM szemely")

curs.execute("SELECT nev,kor,nem FROM szemely WHERE RowID = 1")
curs.execute("SELECT nev,kor FROM szemely WHERE kor>50")

#Adatok módosítása
curs.execute("UPDATE szemely SET nem=?  WHERE nem=?", ("nő","no"))

#Adatok törlése
curs.execute("DELETE FROM szemely WHERE RowID = 11 ")
curs.execute("SELECT * FROM szemely")
pprint(curs.fetchall())

#Az adatok mentése
conn.commit()
conn.close()