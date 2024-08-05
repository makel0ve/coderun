import sys


def main():
    n, k = map(int, input().split())
    m1 = list(map(int, input().split()))
    m2 = list(map(int, input().split()))
    
    
    for i in m2:
        low = 0
        high = len(m1) - 1
        mid = (len(m1) + low) // 2
        while low < high:
            if m1[mid] == i:
                break
            elif m1[mid] > i:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) // 2
        
        if m1[mid] == i:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()