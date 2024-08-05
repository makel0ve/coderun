def dfs_iterative(graph, visited, start):
    stack = [start]
    component = set()

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            component.add(v)
            for neighbor in graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return component

def main():
    n, m = map(int, input().split())
    graph = [set() for _ in range(n + 1)]
    visited = set()
    components = []

    for _ in range(m):
        a, b = map(int, input().split())
        if a != b:
            graph[a].add(b)
            graph[b].add(a)

    for i in range(1, n + 1):
        if i not in visited:
            new_component = dfs_iterative(graph, visited, i)
            components.append(new_component)

    print(len(components))
    for c in components:
        print(len(c))
        print(' '.join(map(str, c)))

if __name__ == "__main__":
    main()
