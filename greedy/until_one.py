n, k = map(int, input().split())

it = 0
while n != 1:
    div, mod = divmod(n, k)
    if mod == 0:
        n //= k
        it += 1
    else:
        n = div
        it += mod + 1
print(it)