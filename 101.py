import sys


def main():
    w, h, n = map(int, input().split())
    low = 0
    high = max(w, h) * n
    
    while high - low > 1:
        mid = (high + low) // 2
        if (mid // h) * (mid // w) >= n:
            high = mid
        else:
            low = mid
        
        
    return high
    
if __name__ == '__main__':
    print(main())