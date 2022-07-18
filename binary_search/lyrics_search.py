# p. 370
# https://school.programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right


def count_by_range(array, left_value, right_value):
    l_idx = bisect_left(array, left_value)
    r_idx = bisect_right(array, right_value)
    return r_idx - l_idx


def solution(words, queries):
    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
    for list in array:
        list.sort()
    for list in reverse_array:
        list.sort()

    answer = []
    for query in queries:
        if query.startswith("?"):
            query = query[::-1]
            left_value = query.replace("?", "a")
            right_value = query.replace("?", "z")
            answer.append(
                count_by_range(reverse_array[len(query)], left_value, right_value)
            )
            continue
        left_value = query.replace("?", "a")
        right_value = query.replace("?", "z")
        answer.append(count_by_range(array[len(query)], left_value, right_value))
    return answer


print(
    solution(
        ["frodo", "front", "frost", "frozen", "frame", "kakao"],
        ["fro??", "????o", "fr???", "fro???", "pro?"],
    )
)
