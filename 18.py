import sys


def main():
    s = input()
    
    try:
        ans = eval(s)
        return ans
    except Exception:
        return "WRONG"

if __name__ == '__main__':
    print(main())