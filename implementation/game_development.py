# p.118

import sys

input = sys.stdin.readline

num_row, num_col = map(int, input().strip().split())
x, y, direction = map(int, input().strip().split())
game_map = [list(map(int, input().strip().split())) for _ in range(num_row)]

y = num_col - y - 1

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

answer = 0

while True:
    org_direction = direction
    if game_map[x][y] != 2:
        game_map[x][y] = 2
        answer += 1
    for _ in range(4):
        direction += 1
        if direction == 4:
            direction = 0
        dx, dy = moves[direction]
        nx = dx + x
        ny = dy + y
        if 0 <= nx < num_row and 0 <= ny < num_col:
            if game_map[nx][ny] in [1, 2]:  # unreachable
                continue
            x, y = nx, ny  # reachable
            break
    if org_direction == direction:
        dx, dy = moves[direction]
        dx = -dx
        dy = -dy
        nx, ny = x + dx, y + dy
        if game_map[nx][ny] == 1:
            break
        x, y = nx, ny

print(answer)
