# Q2 그리디

nums = list(map(int, list(input())))
answer = nums[0]
for num in nums[1:]:
    if answer*num > answer+num:
        answer *= num
    else:
        answer += num
print(answer)