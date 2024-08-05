import sys


def main():
    m1 = set(map(int, input().split()))
    m2 = set(map(int, input().split()))
    
    m3 = list(m2.intersection(m1))
    m3.sort()
    
    s = ' '.join(map(str, m3))
    
    return s

if __name__ == '__main__':
    print(main())