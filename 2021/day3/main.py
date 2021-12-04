items = list()
for line in open("input.txt"):
    bit_array = list(line.strip())
    bit_array = list(map(int, bit_array))
    items.append(bit_array)

bit_sum = list(map(sum, zip(*items)))
item_tot = len(items)

gamma = int(''.join( list(map(lambda x: '1' if x > item_tot/2 else '0', bit_sum))), base=2)
epsilon = int(''.join( list(map(lambda x: '0' if x > item_tot/2 else '1', bit_sum))), base=2)

print(gamma * epsilon)
