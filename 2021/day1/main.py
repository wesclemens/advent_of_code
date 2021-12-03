# Novel
tot = 0
last = None
for number in open("input.txt"):
    number = int(number.strip())
    if not last:
        print(f"{number} (N/A - no previous measurement)")
    elif last < number:
        print(f"{number} (increased)")
        tot += 1
    elif last > number:
        print(f"{number} (decreased)")
    else:
        print(f"{number} (no change)")
    last = number

print(tot)

# Simple
last = None
tot = 0
for number in open("input.txt"):
    number = int(number.strip())
    if last and last < number:
        tot += 1
    last = number
print(tot)
