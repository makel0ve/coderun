import sys


def main():
    m = set(map(str, input().split()))
    n = set(input())
    
    s = n.difference(m)
    
    
    return len(s)
    

if __name__ == '__main__':
    print(main())