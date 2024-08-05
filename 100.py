import sys


def main():
    n, k = map(int, input().split())
    m1 = tuple(map(int, input().split()))
    m2 = tuple(map(int, input().split()))
    
    for i in m2:
        low = 0
        high = n - 1
        while high - low > 1:
            mid = (low + high) // 2
            if m1[mid] > i:
                high = mid
            else:
                low = mid

        if i - m1[low] <= m1[high] - i:
            print(m1[low])
        else:
            print(m1[high])

if __name__ == '__main__':
    main()