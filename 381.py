def main():
    a, b = input().split()
    d = {
        'Monday': '0',
        'Tuesday': '1',
        'Wednesday': '2',
        'Thursday': '3',
        'Friday': '4',
        'Saturday': '5',
        'Sunday': '6'
    }
    start = int(d[b])
    m = ['..' for _ in range(start)]
    s = ''
    
    for i in range(int(a)):
        if i < 9:
            m.append(f'.{i + 1}')
        else:
            m.append(f'{i + 1}')
    

    for i in range(len(m)):
        if i % 7 == 0 and i != 0:
            s += '\n'
        s += f'{m[i]} '
    
    
    return s.strip()
    
if __name__ == "__main__":
    print(main())