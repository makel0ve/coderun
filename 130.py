from collections import OrderedDict


def main():
    f = open('input.txt')
    s = ''
    d = {}
    od = {} 
    
    for line in f:
        s += line
    
    s = s.strip()
    for i in s:
        if i == ' ' or i == '\n':
            continue
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    
    od = OrderedDict(sorted(d.items()))
    ans = [[' '] * (len(od)) for _ in range(max(od.values()) + 1)]
    
    st = 0
    for key, val in od.items():
        ans[max(od.values())][st] = key
        for v in range(val):
            ans[max(od.values()) - 1 - v][st] = '#'
        st += 1
    
    
    return '\n'.join(''.join(i) for i in ans)

    
if __name__ == "__main__":
    print(main())