import csv

with open("src7/favorites/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        fav = row["language"]
        if fav in counts:
            counts[fav] += 1
        else:
            counts[fav] = 1
    for fav in sorted(counts, key=counts.get, reverse=True): #key
        print(f"{fav}: {counts[fav]}")


