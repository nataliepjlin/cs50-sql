from cs50 import SQL

db = SQL("sqlite:///favorites.db")
fav = input("Favorite Problem: ")
rows = db.execute("SELECT COUNT(*) AS count FROM fav WHERE problem = ?", fav)
row = rows[0]
print(row["count"])