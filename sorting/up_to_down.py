# p.178

N = int(input())
num_list = [int(input()) for _ in range(N)]
print(*sorted(num_list, reverse=True))
