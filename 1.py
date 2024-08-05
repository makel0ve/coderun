import sys


def main():
    m = list(map(int, input().split()))
    m.sort()
    return(m[1])

if __name__ == '__main__':
    print(main())