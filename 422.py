import sys


def main():
    a = int(input())
    b = int(input())
    n = int(input())
        
    b2 = b // n if b % n == 0 else b // n + 1
    
    if (a > b2):
        return "YES"
    else: 
        return "NO"
        

if __name__ == '__main__':
    print(main())