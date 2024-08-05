import sys


def main():
    n = int(input())
    n1 = list(map(int, input().split()))
    m = int(input())
    m1 = list(map(int, input().split()))
    d = [[0] * (m + 1) for _ in range(0, n + 1)]
    l = []
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = max(d[i - 1][j], d[i][j - 1])
            if n1[i - 1] == m1[j - 1]:
                d[i][j] = max(d[i][j], d[i - 1][j - 1] + 1)
            
    x = n
    y = m
    while x > 0 and y > 0:
        if n1[x - 1] == m1[y - 1]:
            l.append(n1[x - 1])
            x -= 1
            y -= 1
        elif d[x - 1][y] > d[x][y - 1]:
            x -= 1
        else:
            y -= 1
    
    l.reverse()
    
    return " ".join(map(str, l))
    

if __name__ == '__main__':
    print(main())