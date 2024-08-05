import queue


def main():
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    q1 = queue.Queue()
    q2 = queue.Queue()
    s = 0
    
    for i in s1:
        q1.put(i)
    for i in s2:
        q2.put(i)
        
    while (not q1.empty()) and (not q2.empty()) and (s <= 10**6):
        a = q1.get()
        b = q2.get()
        if a == 0 and b == 9:
            q1.put(a)
            q1.put(b)
            
        elif b == 0 and a == 9:
            q2.put(a)
            q2.put(b)
            
        elif a > b:
            q1.put(a)
            q1.put(b)
            
        elif a < b:
            q2.put(a)
            q2.put(b)
        
        s += 1
        
    if s <= 10**6:
        if q1.empty():
            return f'second {s}'
        else:
            return f'first {s}'
    else:
        return "botva"
    

if __name__ == "__main__":
    print(main())