from collections import deque


def main():
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    d = deque()
    
    for i in range(n):
        if d and d[0] < i - k + 1:
            d.popleft()

        while d and m[d[-1]] >= m[i]:
            d.pop()

        d.append(i)

        if i >= k - 1:
            print(m[d[0]])
    
    
if __name__ == "__main__":
    main()