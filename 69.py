import sys


def main():
    m = tuple(map(int, input().split()))
    score = 0
    
    for i in range(1, len(m) - 1):
        if m[i] > m[i - 1] and m[i] > m[i + 1]:
            score += 1
    
    
    return score


if __name__ == '__main__':
    print(main())