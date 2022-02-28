# p. 312
number = input()
answer = int(number[0])

# for num in number[1:]:
#     answer = max(answer + int(num), answer * int(num))
for num in number[1:]:
    if answer <= 1 or int(num) <= 1:
        answer += int(num)
        continue
    answer *= int(num)

print(answer)