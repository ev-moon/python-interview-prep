from typing import List
from random import randint


# my solution
def selection_sort(li: List) -> List:
    for i in range(len(li)):
        min_idx = i
        for idx, item in enumerate(li[i + 1 :]):
            if item < li[min_idx]:
                min_idx = idx + i + 1
        li[i], li[min_idx] = li[min_idx], li[i]
    return li


# textbook
def selection_sort_answer(li: List) -> List:
    for i in range(len(li)):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_idx]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]
    return li


print(selection_sort_answer([randint(1, 100) for _ in range(10)]))
