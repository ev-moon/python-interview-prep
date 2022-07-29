# p. 570

N = int(input())
numbers = set([1])
cand = 1
while True:
    if len(numbers) == N:
        print(cand)
        break
    cand += 1
    if cand % 2 == 0 and cand // 2 in numbers:
        numbers.add(cand)
    elif cand % 3 == 0 and cand // 3 in numbers:
        numbers.add(cand)
    elif cand % 5 == 0 and cand // 5 in numbers:
        numbers.add(cand)

# solution
ugly = [0] * N
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5
for i in range(1, N):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
print(ugly[-1])
