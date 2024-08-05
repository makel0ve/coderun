import sys


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    start, end = map(int, input().split())    
    visited = [False for _ in range(n)]
    s = [start]
    d = [-1 for _ in range(n)]
    d[start - 1] = 0
    visited[start - 1] = True
    p = [None for _ in range(n)]
    p[start - 1] = -1
    a = []
    
    
    while s != []:
        v = s.pop(0)
    
        for neighbor in range(n):
            if not visited[neighbor] and matrix[v - 1][neighbor] == 1:
                visited[neighbor] = True
                d[neighbor] = d[v - 1] + 1
                s.append(neighbor + 1)
                p[neighbor] = v
    
    
    while end != -1 and (p[end - 1] != None):
        a.append(end)
        end = p[end - 1]

    
    a.reverse()
    path_len = len(a) - 1
    
    if path_len == 0:
        return path_len
    elif path_len > 0:
        path = ' '.join(map(str, a))
        return f'{path_len}\n{path}'
    elif path_len < 0:
        return -1


if __name__ == '__main__':
    print(main())