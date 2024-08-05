import sys


def main():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(0, n)]
    table_d = [[0] * m for _ in range(0, n)]
    table_d[0][0] = table[0][0]
    s = ''
    
    for i in range(1, n):
        table_d[i][0] = table_d[i - 1][0] + table[i][0]
    for i in range(1, m):
        table_d[0][i] = table_d[0][i - 1] + table[0][i]
        
    for i in range(1, n):
        for j in range(1, m):
            table_d[i][j] = max(table_d[i - 1][j], table_d[i][j - 1]) + table[i][j]
            
    x, y = n - 1, m - 1
    while x >= 0 and y >= 0:
        if x == 0 and y == 0:
            break
        if x == 0:
            y -= 1
            s += "R"
        elif y == 0:
            x -= 1
            s += "D"
        elif table_d[x - 1][y] > table_d[x][y - 1] and y != 0:
            x -= 1
            s += "D"
        elif table_d[x - 1][y] <= table_d[x][y - 1] and x != 0:
            y -= 1
            s += "R"
    
    s = s[::-1]
    
    if s == '':
        return f'{table_d[-1][-1]}'
    else:
        return f'{table_d[-1][-1]}\n{s}'

if __name__ == '__main__':
    print(main())