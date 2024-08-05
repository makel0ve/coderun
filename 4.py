import sys


def main():
    n, m = map(int, input().split())
    table = [[0] * m for _ in range(0, n)]
    table[0][0] = 1
    
    for i in range(2, n, +2):
        for j in range(1, m, +1):
            table[i][j] += table[i - 2][j - 1]
    
    for i in range(1, n, +1):
        for j in range(2, m, +2):
            table[i][j] += table[i - 1][j - 2]

    for i in range(3, n):
        for j in range(3, m):
            table[i][j] = table[i - 1][j - 2] + table[i - 2][j - 1]
            
    
    return table[-1][-1]

if __name__ == '__main__':
    print(main())