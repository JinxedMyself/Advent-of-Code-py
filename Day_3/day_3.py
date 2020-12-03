# day 3
# i dont like where this is going
# it involves map n stuff
import math

map_file = open(r"Day_3\trees_map.txt", "r")
# for some reason this works with raw and i dont like this
trees = 0
x_pos = 0
y_pos = 0
right_move = 3
down_move = 1
map_lines = []

for line in map_file:
    map_lines.append(line.strip())

# part 1
for x in range(math.floor(len(map_lines)/down_move)):
    if (map_lines[y_pos])[x_pos] == "#":
        trees += 1
    x_pos += right_move
    y_pos += down_move
    if x_pos >= len(map_lines[x]):
        x_pos = x_pos-len(map_lines[x])

print(f"Trees: {trees}")