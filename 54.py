def main():
    n = int(input())
    d = dict()
    for _ in range(n):
        m = int(input())
        for _ in range(m):
            language = input()
            if d.get(language):
                d[language] += 1
            else:
                d[language] = 1
                
    s2 = set(key for key, val in d.items() if val == n)
    
    ans = f'{len(s2)}\n{'\n'.join(s2)}\n{len(d.keys())}\n{'\n'.join(d.keys())}'
    

    return ans
    

if __name__ == "__main__":
    print(main())