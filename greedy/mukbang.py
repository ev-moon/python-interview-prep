# p. 316

from collections import defaultdict


def solution(food_times, k):
    cycles = 0
    food_map = defaultdict(list)
    for idx, time in enumeate(food_times):
        food_map[time].append(idx)
    total_food = len(food_times)
    popped = []
    pop_extend = []
    while k > 0:
        next_cycle = min(food_map.keys())
        k -= (next_cycle - cycles) * (total_food - len(popped))
        cycles = next_cycle
        pop_extend = food_map.pop(next_cycle)
        popped.extend(pop_extend)

    pointer = popped[-1]
    for _ in range(-k):
        pointer -= 1
        while pointer in popped[: -len(pop_extend)]:
            pointer -= 1
    return pointer % len(food_times) + 1
