# p.223


def solution():
    N = int(input())

    if N == 1:
        return 1 % 796796

    array = [0] * N
    array[0] = 1
    array[1] = 3
    for idx in range(2, N):
        array[idx] = array[idx - 2] * 2 + array[idx - 1]

    return array[-1] % 796796


print(solution())
