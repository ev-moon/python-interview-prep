# p.182

length, switches = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))
array_a.sort()
array_b.sort()
added = 0
for i in range(switches):
    diff = array_b[-(i + 1)] - array_a[i]
    if diff < 0:
        break
    added += diff
print(sum(array_a) + added)
