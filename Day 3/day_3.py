# day 3
# i dont like where this is going
# it involves map n stuff
import math

map_file = open("map.txt", "r")
trees = 0
x_pos = 0
y_pos = 0
right_move = 3
down_move = 1
map_lines = []

for line in map_file:
    map_lines.append(line.strip())
