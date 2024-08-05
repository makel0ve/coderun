import queue


def main():
    q = queue.Queue()
    ans = ''
    while True:

        s = input().split()
        if 'exit' in s:
            ans += 'bye'
            return ans
        elif "push" in s:
            q.put(int(s[1]))
            ans += 'ok\n'
        elif 'pop' in s:
            if q.empty():
                ans += 'error\n'
            else:
                n = q.get()
                ans += f'{str(n)}\n'
        elif 'front' in s:
            if q.empty():
                ans += 'error\n'
            else:
                ans += f'{str(q.queue[0])}\n'
        elif 'size' in s:
            ans += f'{str(q.qsize())}\n'
        elif 'clear' in s:
            while not q.empty():
                q.get()
            ans += 'ok\n'
        

if __name__ == "__main__":
    print(main())