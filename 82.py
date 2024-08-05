def main():
    q1, q2 = map(int, input().split())
    r = input()
    
    return q2 if (r == "auto") or (r == "heat" and q1 < q2) or (r == "freeze" and q1 > q2) else q1

if __name__ == "__main__":
    print(main())