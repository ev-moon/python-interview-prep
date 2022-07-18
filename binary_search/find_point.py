# p.368


def binary_search(array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        if array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1


N = int(input())
numbers = list(map(int, input().split()))
start = 0
end = N - 1
print(binary_search(numbers))
