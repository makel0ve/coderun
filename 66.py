import sys


def main():
    m = list(map(int, input().split()))
    min1 = m[0]
    min2 = m[1]
    max1 = m[0]
    max2 = m[1]
    
    for i in range(1, len(m)):
        if min1 >= m[i]:
            min2 = min1
            min1 = m[i]
        if min2 >= m[i] and m[i] > min1:
            min2 = m[i]
        if max1 <= m[i]:
            max2 = max1
            max1 = m[i]
        if max2 <= m[i] and m[i] < max1:
            max2 = m[i]
            

    if min1 * min2 > max1 * max2:
        return f'{min1} {min2}'
    else:
        return f"{max2} {max1}"
    

if __name__ == '__main__':
    print(main())