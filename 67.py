import sys


def main():
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    
    for i in range(len(l)):
        if l[i:] == l[i:][::-1]:
            print(i)
            if i != 0:
                print(*l[:i][::-1])
            break

if __name__ == '__main__':
    main()