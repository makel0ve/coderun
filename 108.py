import sys


def main():
    n, l = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(0, n):
        for j in range(i + 1, n):
            a = m[i] + m[j]
            a.sort()
            print(a[l - 1])


if __name__ == '__main__':
    main()