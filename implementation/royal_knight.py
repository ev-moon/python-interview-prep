# p. 115

x_pos, y_pos = input()
x_axis = ["a", "b", "c", "d", "e", "f", "g", "h"]

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
x_pos = x_axis.index(x_pos)
y_pos = int(y_pos) - 1

answer = 0

for dx, dy in moves:
    if 0 <= dx + x_pos < 8 and 0 <= dy + y_pos < 8:
        answer += 1

print(answer)