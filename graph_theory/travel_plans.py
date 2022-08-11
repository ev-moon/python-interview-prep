# p. 393
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def main():
    n_nodes, n_plan = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n_nodes)]
    plan = list(map(int, input().split()))

    parent = [i for i in range(n_nodes + 1)]
    for i in range(n_nodes):
        for j in range(n_nodes):
            if graph[i][j] == 1:
                union_parent(parent, i + 1, j + 1)

    for i in range(n_plan - 1):
        if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
            print("NO")
            return
    print("YES")


main()