import random

flips = []
for flip in range(10000):
    if random.randint(0, 1) == 0:
        flips.append("H")
    else:
        flips.append("T")

streak = 0
for i in range(len(flips)):
    if " ".join(flips[i:i + 6]) == "H H H H H H" or " ".join(flips[i:i + 6]) == "T T T T T T":
        streak += 1

print(f"Chance of streak of six is: {streak / 100}%.")
