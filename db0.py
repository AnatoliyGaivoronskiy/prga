import sqlite3

databaze = sqlite3.connect("hra.db")
print("SQL konzole. Piš příkazy, ukonči slovem konec.")

while True:
    prikaz = input("sql> ")
    if prikaz.strip().lower() == "konec":
        break
    try:
        kurzor = databaze.execute(prikaz)
        radky = kurzor.fetchall()
        if kurzor.description:
            print(" | ".join(sloupec[0] for sloupec in kurzor.description))
        for radek in radky:
            print(" | ".join(str(hodnota) for hodnota in radek))
        databaze.commit()
        print(f"({len(radky)} řádků)")
    except sqlite3.Error as chyba:
        print("CHYBA:", chyba)

databaze.close()
