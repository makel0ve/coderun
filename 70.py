import sys


def main():
    n = int(input())
    m = list(map(int, input().split()))
    x = int(input())
    s = 2002
    a = 0
    
    for i in m:
        if abs(x - i) < s:
            s = abs(x - i)
            a = i

    return a

if __name__ == '__main__':
    print(main())