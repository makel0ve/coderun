def main():
    n, _ = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    
    for i in x:
        low = 0
        high = n - 1
        while high - low > 1:
            mid = (low + high) // 2
            if a[mid] >= i:
                high = mid
            else:
                low = mid
            
        if i - a[low] <= a[high] - i:
            print(low + 1)
        else:
            print(high + 1)
    
    
if __name__ == '__main__':
    main()