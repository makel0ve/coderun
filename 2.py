import sys


def main():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(0, n)]
    table_d = [[0] * m for _ in range(0, n)]
    
    table_d[0][0]=table[0][0]
    
    for i in range(1, n):
        table_d[i][0] = table_d[i - 1][0] + table[i][0]
    for i in range(1, m):
        table_d[0][i] = table_d[0][i - 1] + table[0][i]
        
    for i in range(1, n):
        for j in range(1, m):
            table_d[i][j] = min(table_d[i][j - 1], table_d[i - 1][j]) + table[i][j]
    
    return table_d[-1][-1]
    
if __name__ == '__main__':
    print(main())