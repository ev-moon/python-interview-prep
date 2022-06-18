# p.351
# https://www.acmicpc.net/problem/18428

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
map = [list(input().split()) for _ in range(N)]


def get_obstacle_coords():
    coords = []
    for i in range(N):
        for j in range(N):
            if map[i][j] == "X":
                coords.append((i, j))
    return coords


def dfs(x, y):
    for i in range(x - 1, -1, -1):
        if map[i][y] == "O" or map[i][y] == "T":
            break
        if map[i][y] == "S":
            return True
    for i in range(y - 1, -1, -1):
        if map[x][i] == "O" or map[x][i] == "T":
            break
        if map[x][i] == "S":
            return True
    for i in range(x + 1, N):
        if map[i][y] == "O" or map[i][y] == "T":
            break
        if map[i][y] == "S":
            return True
    for i in range(y + 1, N):
        if map[x][i] == "O" or map[x][i] == "T":
            break
        if map[x][i] == "S":
            return True
    return False


def try_iteration(map):
    for i in range(N):
        for j in range(N):
            if map[i][j] == "T":
                if dfs(i, j):
                    return False
    return True


for obstacle_trio in combinations(get_obstacle_coords(), 3):
    co1, co2, co3 = obstacle_trio
    map[co1[0]][co1[1]] = "O"
    map[co2[0]][co2[1]] = "O"
    map[co3[0]][co3[1]] = "O"
    if try_iteration(map):
        print("YES")
        sys.exit(0)
    map[co1[0]][co1[1]] = "X"
    map[co2[0]][co2[1]] = "X"
    map[co3[0]][co3[1]] = "X"
print("NO")
