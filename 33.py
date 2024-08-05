def main():
    s1 = input()
    s2 = input()
    mat = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    for i in range(1, len(s1) + 1):
        mat[i][0] = i
        
    for i in range(1, len(s2) + 1):
        mat[0][i] = i
        
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] != s2[j - 1]:
                mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1] + 1)
            else:
                mat[i][j] = min(mat[i - 1][j] + 1, mat[i][j - 1] + 1, mat[i - 1][j - 1])
        
    return mat[-1][-1]
    
if __name__ == '__main__':
    print(main())