import sys


def main():
    n, m, k = map(int, input().split())
    matrix = [[0] * (m + 2) for _ in range(n + 2)]
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    s = ''
    
    for _ in range(k):
        p, q = map(int, input().split())
        matrix[p][q] = '*'
        
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == '*':
                for dest in range(8):
                    if matrix[i+(di[dest])][j+(dj[dest])] != None and matrix[i+(di[dest])][j+(dj[dest])] != '*':
                        matrix[i+(di[dest])][j+(dj[dest])] += 1
    
    
    for i in range(1, n+1):
        s += ' '.join(map(str, matrix[i][1:m+1]))
        s += "\n"
    
    
    return s.strip()


if __name__ == '__main__':
    print(main())