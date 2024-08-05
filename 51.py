from collections import Counter


def main():
    f = open("input.txt")
    s = ''
    ans = []
    for line in f:
        s += line.replace('\n', ' ')
    m = list(map(str, s.split()))    
    d = dict(Counter(m))

    for i in range(len(m) - 1, -1, -1):
        ans.append(f'{d[m[i]] - 1}')
        d[m[i]] -= 1


    return ' '.join(map(str, ans[::-1])).strip()


if __name__ == "__main__":
    print(main())