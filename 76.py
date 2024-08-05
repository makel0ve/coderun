import sys


def main():
    n, k, m = map(int, input().split())
    s = 0
    
    
    if m > k:
        return s    
    
    while n >= k:
        n -= k
        s += k // m
        n += k % m
    
    
    return s

if __name__ == '__main__':
    print(main())