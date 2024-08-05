def main():
    a = int(input())
    b = int(input())
    c = int(input())
    
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "YES"
    
    return "NO"


if __name__ == '__main__':
    print(main())