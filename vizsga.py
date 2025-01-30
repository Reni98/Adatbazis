import sqlite3
from pprint import pprint
conn = sqlite3.connect("vizsga.db")
curs = conn.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS vizsgazok (ozonosito INTEGER, nev TEXT, szulido INTEGER, pontszam REAL) ")
# curs.execute("INSERT INTO vizsgazok VALUES (7223231, 'John Doe', 1995, 70.4)")
# curs.execute("INSERT INTO vizsgazok VALUES (7656565, 'Jane Doe', 1995, 75.4)")
# curs.execute("INSERT INTO vizsgazok VALUES (7545532, 'Proba Elek', 1997, 50.6)")
# curs.execute("INSERT INTO vizsgazok VALUES (7934334, 'Kovács János', 2000, 90.4)")
# curs.execute("INSERT INTO vizsgazok VALUES (7434332, 'Proba Kinga', 2001, 56.6)")

# curs.execute("SELECT * FROM vizsgazok")
#Azokat a személyek és nevek lesznek megjelenítve akiknek a pontszáma több,mint 56.6
# curs.execute("SELECT nev,pontszam FROM vizsgazok WHERE pontszam > 56.6")
#Az a név kerül megjelenítésre ami P betűvel kezdődik
# curs.execute("SELECT nev FROM vizsgazok WHERE nev Like 'P%'")
#Visszaadja melyik a legkisebb pontszám
# curs.execute("SELECT MIN(pontszam)  FROM vizsgazok")
#Visszaadja melyik a legnagyobb pontszámot
# curs.execute("SELECT MAX(pontszam) FROM vizsgazok")
#A SUM összeadja a pontszámokat
# curs.execute("SELECT SUM(pontszam) FROM vizsgazok")
#A pontszámok átlagát számoja meg
# curs.execute("SELECT AVG(pontszam) FROM vizsgazok")
curs.execute("UPDATE vizsgazok SET nev='Kiss Jenő' WHERE RowID = 8 ")
curs.execute("UPDATE vizsgazok SET szulido=2004 WHERE nev = 'Kiss Jenő'")
curs.execute("DELETE FROM vizsgazok WHERE RowID = 9")
curs.execute("DELETE FROM vizsgazok WHERE RowID = 7")

curs.execute("SELECT * FROM vizsgazok")

pprint(curs.fetchall())

conn.commit()
conn.close()

#Feladat
# Hozzatok létre egy kereskedes nevű adatbázist a tábla neve autok legyen
#A mezők nevei: jogositvanyszam, vasarloneve, autorendszama, ar,tipus
# (10 sor különböző adat)
#Jelenítsétek meg azokat a neveket amelyek T-vel kezdődik
#Melyik a legdrábább
#Mennyi volt a bevétel
#Azokat is írjátok ki azokat az autókat amik 10 millónál drágább

