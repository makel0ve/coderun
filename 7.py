import sys


def main():
    n, m = map(int, input().split())
    graf = {key: set() for key in range(1, n + 1)}
    visited = [False] * n
    s = []
    visited[0] = True
    s.append(graf[1])
    l = [1]
    
    for _ in range(0, m):
        a1, a2 = map(int, input().split())
        graf[a1].add(a2)
        graf[a2].add(a1)
        
    
    while s != []:
        v = s.pop()
        for i in v:
            if not visited[i - 1]:
                visited[i - 1] = True
                s.append(graf[i])
                l.append(i)
        if not False in visited:
            s = []
        
    l.sort()
    
    return f'{len(l)}\n{' '.join(map(str, l))}'

    
if __name__ == '__main__':
    print(main())