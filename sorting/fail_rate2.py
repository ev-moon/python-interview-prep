def solution(N, stages):
    fail_rate = []
    stage_arrived = [0] * (N + 1)
    for s in stages:
        stage_arrived[s - 1] += 1
    arrived_till_now = stage_arrived[-1]
    for idx, num_p in enumerate(stage_arrived[:-1][::-1]):
        fail_rate.append((num_p / (num_p + arrived_till_now), N - idx))
        arrived_till_now += num_p
    fail_rate.sort(key=lambda x: (-x[0], x[1]))
    return [x[1] for x in fail_rate]


print(solution())
