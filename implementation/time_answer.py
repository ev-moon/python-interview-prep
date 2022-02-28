hour = int(input())

# Brute Force
count = 0
for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            if "3" in "".join(str(item) for item in [h, m, s]):
                count += 1
print(count)
