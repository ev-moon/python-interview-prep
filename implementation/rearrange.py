# p.322

string = input()
alpha_list = []
num_sum = 0
for s in string:
    if s.isalpha():
        alpha_list.append(s)
    else:
        num_sum += int(s)
alpha_list.sort()
answer = "".join(alpha_list) + str(num_sum)
print(answer)