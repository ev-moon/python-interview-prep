import sys

input = sys.stdin.readline

N = int(input().strip())
moves = list(input().strip().split())

move_dict = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
pos_x = pos_y = 0

for move in moves:
    dx, dy = move_dict[move]
    if 0 <= pos_x + dx < N and 0 <= pos_y + dy < N:
        pos_x += dx
        pos_y += dy

print(str(pos_x + 1) + " " + str(pos_y + 1))
