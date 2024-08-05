from collections import Counter


def main():
    _ = int(input())
    a = map(int, input().split())
    c = Counter(a)
    max_val = max(c.values())
    max_key = max(i for i, j in c.items() if j == max_val)
    
    return max_key


if __name__ == "__main__":
    print(main())