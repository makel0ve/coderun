import sys


def main():
    j = set(input().strip())
    s = input().strip()
    d = 0
    
    for i in j:
        d += s.count(i)
    
    return d

if __name__ == '__main__':
    print(main())