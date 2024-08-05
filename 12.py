import sys


def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    start, end = map(int, input().split())
    s = [start]
    d = [-1 for _ in range(n)]
    d[start - 1] = 0
    visited = [False for _ in range(n)]
    visited[start - 1] = True
    
    
    while s != []:
        v = s.pop(0)
                
        if v == end:
            return d[v - 1]
                
        for neighbor in range(n):
            if matrix[v - 1][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                d[neighbor] = d[v - 1] + 1
                s.append(neighbor + 1)
                
    return -1
    
if __name__ == '__main__':
    print(main())