from collections import Counter
import sys


def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    m = Counter(a)
    s = [i for i in m.values() if i == 1]
    
    return len(s)

if __name__ == '__main__':
    print(main())