import heapq


def main():
    n = int(input())
    m = list(map(int, input().split()))
    h = heapq.nsmallest(n, m)
    
    return ' '.join(map(str, h))


if __name__ == "__main__":
    print(main())