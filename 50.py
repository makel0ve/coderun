from collections import Counter


def main():
    # m = list(map(str, input().split()))
    k = ''
    f = open("input.txt")
    for line in f:
        k += line
    k = k.strip().replace('\n', ' ')
    m = list(map(str, k.split()))
    s = Counter(m)
    max_elem = max(s.values())

    a = min([key for key, val in s.items() if val == max_elem])

    return a
    
if __name__ == "__main__":
    print(main())