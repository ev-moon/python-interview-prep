# p.355
# https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque


def solution(board):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([[(0, 0), (0, 1), 0, True]])  # (pos_a, pos_b, moves, is_horizontal)
    h_turns = [
        [(0, 1), (0, 1), (1, 0)],
        [(1, 1), (0, 0), (1, -1)],
        [(-1, 1), (-1, 0), (0, -1)],
        [(-1, 0), (1, -1), (0, 0)],
    ]
    v_turns = [
        [(1, -1), (0, 0), (1, 1)],
        [(-1, -1), (1, -1), (0, 0)],
        [(1, -1), (0, -1), (-1, 0)],
        [(1, 1), (0, 0), (-1, +1)],
    ]
    N = len(board) - 1

    def valid_pos(coord):
        for x in coord:
            if x < 0 or x > N:
                return False
        return True

    while queue:
        pos_a, pos_b, n_moves, is_horzontal = queue.popleft()
        if pos_a == (N, N) or pos_b == (N, N):
            return n_moves
        for dx, dy in moves:
            na_x, na_y = pos_a[0] + dx, pos_a[1] + dy
            nb_x, nb_y = pos_b[0] + dx, pos_b[1] + dy
            if valid_pos([na_x, na_y, nb_x, nb_y]):
                queue.append([(na_x, na_y), (nb_x, nb_y), n_moves + 1, is_horzontal])
            if is_horzontal:
                turns = h_turns
            else:
                turns = v_turns
            for cond, dx_a, dx_b in turns:
                if (
                    valid_pos([pos_a[0] + cond[0], pos_a[1] + cond[1]])
                    and board[pos_a[0] + cond[0]][pos_a[1] + cond[1]] != 1
                ):
                    na_x, na_y = pos_a[0] + dx_a[0], pos_a[1] + dx_a[1]
                    nb_x, nb_y = pos_b[0] + dx_b[0], pos_b[1] + dx_b[1]
                    if valid_pos([na_x, na_y, nb_x, nb_y]):
                        queue.append(
                            [(na_x, na_y), (nb_x, nb_y), n_moves + 1, ~is_horzontal]
                        )


print(
    solution(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)
