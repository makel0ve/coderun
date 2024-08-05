def main():
    n, k = map(int, input().split())
    m = [0] * (n + k)
    m[0] = 1
    
    for i in range(1, n):
        for j in range(k):
            m[j + i] += m[i - 1]

    
    return m[-k - 1]


if __name__ == "__main__":
    print(main())