def insert_elem(m, e):
    i = len(m)
    m.append(e)
    while i > 0 and m[i // 2] < e:
        m[i] = m[i // 2]
        i = i // 2
        m[i] = e

    return m
    

def extract_elem(m):
    if len(m) == 1:
        return m.pop()
    root = m[0]
    m[0] = m.pop()
    i = 0
    while 2 * i + 1 < len(m) and m[i] < max(m[2 * i], m[2 * i + 1]):
        if m[2 * i] > m[2 * i + 1]:
            m[i], m[2 * i] = m[2 * i], m[i]
            i = 2 * i
        else:
            m[i], m[2 * i + 1] = m[2 * i + 1], m[i]
            i = 2 * i + 1
    if 2 * i == len(m) - 1 and m[i] < m[2 * i]:
        m[i], m[2 * i] = m[2 * i], m[i]
    return root


def main():
    m = []
    s = ''
    n = int(input())
    for _ in range(n):
        a = list(map(int, input().split()))
        if len(a) == 2:
            insert_elem(m, a[1])
        else:
            s += f"{extract_elem(m)}\n"

    return s.strip()


if __name__ == "__main__":
    print(main())