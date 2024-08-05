import sys


def main():
    m = list(map(int, input().split()))
    m.sort()
    
    a = m[0] * m[1] * m[-1]
    b = m[-1] * m[-2] * m[-3]
    
    if a > b:
        return f"{m[0]} {m[1]} {m[-1]}"
    else:
        return f"{m[-1]} {m[-2]} {m[-3]}"

if __name__ == '__main__':
    print(main())