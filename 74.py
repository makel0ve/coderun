import sys


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    
    if a <= d and b <= e or a <= e and b <= d:
        return "YES"
    if b <= d and c <= e or b <= e and c <= d:
        return 'YES'
    if a <= d and c <= e or a <= e and c <= d:
        return 'YES'
    
    return "NO"


if __name__ == '__main__':
    print(main())