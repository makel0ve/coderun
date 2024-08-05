from collections import deque


def main():
    d = deque()
    ans = ''

    while True:
        s = input()
        if 'exit' in s:
            ans += 'bye'
            break
        elif 'push_front' in s:
            n = s.split()[1]
            d.appendleft(int(n))
            ans += "ok\n"
        elif 'push_back' in s:
            n = s.split()[1]
            d.append(int(n))
            ans += "ok\n"
        elif 'pop_front' in s:
            if len(d) == 0:
                ans += "error\n"
            else:
                n = d.popleft()
                ans += f"{n}\n"
        elif 'pop_back' in s:
            if len(d) == 0:
                ans += "error\n"
            else:
                n = d.pop()
                ans += f"{n}\n"
        elif 'front' in s:
            if len(d) == 0:
                ans += "error\n"
            else:
                ans += f"{d[0]}\n"
        elif 'back' in s:
            if len(d) == 0:
                ans += "error\n"
            else:
                ans += f"{d[-1]}\n"
        elif 'size' in s:
            ans += f"{len(d)}\n"
        elif 'clear' in s:
            d.clear()
            ans += "ok\n"
    
    return ans


if __name__ == "__main__":
    print(main())