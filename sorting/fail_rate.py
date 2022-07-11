# p. 361
# https://programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter


def solution(N, stages):
    previous_stage_N = 0
    fail_rate = Counter()
    total = len(stages)
    count_dict = Counter(stages)
    for stage in range(1, N + 1):
        curr_stage_N = count_dict.get(stage, 0)
        if curr_stage_N == 0:
            fail_rate[stage] = 0
            continue
        fail_rate[stage] = curr_stage_N / (total - previous_stage_N)
        previous_stage_N += curr_stage_N
    return [k for k, _ in fail_rate.most_common(N)]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
