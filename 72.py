import sys


def main():
    m = tuple(map(int, input().split()))
    
    for i in range(1, len(m)):
        if m[i] <= m[i - 1]:
            return "NO"
        
    return "YES"


if __name__ == '__main__':
    print(main())