from collections import Counter, OrderedDict


def main():
    d = {}
    f = open("input.txt")
    for line in f:
        k = line.split()
        if not d.get(k[0]):
            d[k[0]] = {k[1]: int(k[2])}
        else:
            if d[k[0]].get(k[1]):
                d[k[0]][k[1]] += int(k[2])
            else:
                d[k[0]][k[1]] = int(k[2])
            
    for key, val in d.items():
        d[key] = sorted(val.items())
    
    d = dict(sorted(d.items()))
    
    for key, val in d.items():
        print(f"{key}:")
        for v in val:
            print(f"{v[0]} {v[1]}")
    


if __name__ == "__main__":
    main()