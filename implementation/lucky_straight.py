# p.321

points = input()
left_sum = right_sum = 0
for n in points[: len(points) // 2]:
    left_sum += int(n)
for n in points[len(points) // 2 :]:
    right_sum += int(n)
result = "LUCKY" if left_sum == right_sum else "READY"
print(result)
