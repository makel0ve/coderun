def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s1, s2 = map(str, input().split())
        d[s1] = s2
        d[s2] = s1
        
    s = input()
    
    return d[s]
        

if __name__ == "__main__":
    print(main())