# https://www.acmicpc.net/problem/18310


def my_solution():
    num_houses = int(input())
    houses = list(map(int, input().split()))
    houses.sort()
    if num_houses % 2 != 0:
        mid = num_houses // 2
    else:
        mid = num_houses // 2 - 1
    print(houses[mid])


def simpler_solution():
    num_houses = int(input())

    houses = list(map(int, input().split()))
    houses.sort()

    print(houses[(num_houses - 1) // 2])
