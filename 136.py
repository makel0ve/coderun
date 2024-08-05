from datetime import datetime, timedelta


def main():
    a = datetime.strptime(input(), "%H:%M:%S")
    b = datetime.strptime(input(), "%H:%M:%S")
    c = datetime.strptime(input(),  "%H:%M:%S")
    
    if c < a:
        c += timedelta(days=1)
    e = c - a
    d = b + (e // 2)
    
    ans = d if e.seconds % 2 == 0 else d + timedelta(seconds=1)
    ans = datetime.strftime(ans, "%H:%M:%S")    

    
    return ans


if __name__ == "__main__":
    print(main())