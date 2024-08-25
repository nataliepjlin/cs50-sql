import csv

from collections import Counter

with open("src7/favorites/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = Counter()
    for row in reader:
        fav = row["language"]
        counts[fav] += 1
    for fav, count in counts.most_common(): #key
        print(f"{fav}: {count}")


