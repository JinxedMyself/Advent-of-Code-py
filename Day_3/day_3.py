# i dont like where this is going
# it involves map n stuff
import math

map_file = open(r"Day_3\trees_map.txt", "r")
# for some reason this works with raw and i dont like this
trees = 0
x_pos = 0
y_pos = 0
moves = [[1,1], [3,1], [5,1], [7,1], [1,2]]
trees = 0
parttwo_trees = [[0], [0], [0], [0], [0]]
# [right_move, down_move]
map_lines = []

for line in map_file:
    map_lines.append(line.strip())

# part 1
# for x in range(math.floor(len(map_lines)/moves[1][1])):
#     if (map_lines[y_pos])[x_pos] == "#":
#         trees += 1
#     x_pos += moves[1][0]
#     y_pos += moves[1][1]
#     if x_pos >= len(map_lines[x]):
#         x_pos = x_pos-len(map_lines[x])

# print(f"Trees: {trees}")

for z in range(len(moves)):
    x_pos = 0
    y_pos = 0
    for x in range(math.floor(len(map_lines)/moves[z][1])):
        if (map_lines[y_pos])[x_pos] == "#":
            parttwo_trees[z] += 1
        x_pos += moves[z][0]
        y_pos += moves[z][1]
        if x_pos >= len(map_lines[x]):
            x_pos = x_pos-len(map_lines[x])

print(f"Trees: {parttwo_trees}")