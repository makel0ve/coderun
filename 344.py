import sys


def main():
    n, m = map(int, input().split())
    matrix = list([None] * (m + 2) for _ in range(n + 2))
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]
    di2 = [-2, -2, 2, 2]
    dj2 = [-2, 2, -2, 2]
    
    w = int(input())
    for _ in range(w):
        i, j = map(int, input().split())
        matrix[i][j] = "white"
            
    b = int(input())
    for _ in range(b):
        i, j = map(int, input().split())
        matrix[i][j] = "black"
    
    forward = input()

    if forward == "white":
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i][j] == "white":
                    for k in range(4):
                        if matrix[i + (di[k])][j + (dj[k])] == "black":
                            if ((i + (di2[k])) > 0 and (i + (di2[k])) < n + 1) and \
                                ((j + (dj2[k])) > 0 and (j + (dj2[k])) < m + 1) and \
                                matrix[i + (di2[k])][j + (dj2[k])] == None:
                                return "Yes"
    else:
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i][j] == "black":
                    for k in range(4):
                        if matrix[i + (di[k])][j + (dj[k])] == "white":
                            if ((i + (di2[k])) > 0 and (i + (di2[k])) < n + 1) and \
                                ((j + (dj2[k])) > 0 and (j + (dj2[k])) < m + 1) and \
                                matrix[i + (di2[k])][j + (dj2[k])] == None:
                                return "Yes"
    
    return "No"
    
if __name__ == '__main__':
    print(main())