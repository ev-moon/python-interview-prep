# p.346
# https://programmers.co.kr/learn/courses/30/lessons/60058


def reverse(p):
    li = []
    for x in p:
        if x == "(":
            li.append(")")
        else:
            li.append("(")
    return "".join(li)


def solution(p):
    if not p:
        return p
    num_l = num_r = 0
    stack = []
    for x in p:
        if x == "(":
            num_l += 1
        else:
            num_r += 1
        if stack and stack[-1] == "(" and x == ")":
            stack.pop()
        else:
            stack.append(x)
        if num_l == num_r:
            if not stack:
                return p[: num_l * 2] + solution(p[num_l * 2 :])
            return "(" + solution(p[num_l * 2 :]) + ")" + reverse(p[1 : num_l * 2 - 1])


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
print(solution("(())"))
print(solution("()"))
print(solution("((()))()"))
