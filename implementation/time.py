hour = int(input())

# Analytical Thinking
hourly_counts = 15 * 45 + 15 * 60

if hour < 3:
    answer = (hour + 1) * hourly_counts
elif hour < 13:
    answer = hour * hourly_counts + 60 * 60
elif hour < 23:
    answer = (hour - 1) * hourly_counts + 60 * 60 * 2
else:  # hour == 23
    answer = (hour - 2) * hourly_counts + 60 * 60 * 3

print(answer)
