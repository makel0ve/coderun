import sys


def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(m)]
    
    both = set(a).intersection(set(b))
    both = list(both)
    both.sort()
    print(len(both))
    print(' '.join(map(str, both)))
    
    a = set(a).difference(both)
    a = list(a)
    a.sort()
    print(len(a))
    print(' '.join(map(str, a)))
    
    b = set(b).difference(both)
    b = list(b)
    b.sort()
    print(len(b))
    print(' '.join(map(str, b)))
    

if __name__ == '__main__':
    main()