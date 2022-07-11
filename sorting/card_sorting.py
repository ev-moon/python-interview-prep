# https://www.acmicpc.net/problem/1715

import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline
N = int(input())
cards = [int(input()) for _ in range(N)]


def get_num_ops(cards):
    ops = 0
    heapify(cards)
    while cards:
        card_bunch_1 = heappop(cards)
        if not cards:
            return ops
        card_bunch_2 = heappop(cards)
        ops += card_bunch_1 + card_bunch_2
        heappush(cards, card_bunch_1 + card_bunch_2)


print(get_num_ops(cards))
