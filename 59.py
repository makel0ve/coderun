import sys


def main():
    m = ''
    for line in sys.stdin:
        if line.rstrip() == '':
            break
        m += line
        
    m = set(m.split())

    return len(m)


if __name__ == '__main__':
    print(main())