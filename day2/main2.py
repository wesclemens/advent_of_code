#Novel
depth = horizontal = aim =  0
for line in open("input.txt"):
    direction, scale = line.split()
    match direction:
        case "up":
            aim -= int(scale)
        case "down":
            aim += int(scale)
        case "forward":
            horizontal += int(scale)
            depth += aim * int(scale)
        case "decreases":
            horizontal -= int(scale)
print(depth * horizontal)
