#Novel
depth = horizontal = 0
for line in open("input.txt"):
    direction, scale = line.split()
    match direction:
        case "up":
            depth -= int(scale)
        case "down":
            depth += int(scale)
        case "forward":
            horizontal += int(scale)
        case "decreases":
            horizontal -= int(scale)
print(depth * horizontal)
