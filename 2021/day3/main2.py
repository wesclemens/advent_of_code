items = list()
for line in open("2021/day3/input.txt"):
    bit_array = list(line.strip())
    bit_array = list(map(int, bit_array))
    items.append(bit_array)


def find_value(items, desired):
    for pos in range(len(items[0])):
        if len(items) == 1:
            break
        bit_sum = sum( x[pos] for x in items)
        item_tot = len(items)
        desired_vaule = desired if bit_sum >= item_tot/2 else int(not bool(desired))
        remaining_items = len(items)
        for enum, item in enumerate(items[::-1]):
            if desired_vaule != item[pos]:
                del items[remaining_items - enum - 1]
    return items[0]

print(int(''.join(map(str, find_value(items.copy(), 1))), base=2) * int(''.join(map(str, find_value(items.copy(), 0))), base=2))
