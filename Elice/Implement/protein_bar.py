def protein(bar):

    weights = [250, 40, 10]
    counts = [0,0,0]
    if bar < 10:
        return -1

    while bar >= 10:
        if bar >= weights[0]:
            bar -= weights[0]
            counts[2] += 1
        elif bar >= weights[1]:
            bar -= weights[1]
            counts[1] += 1
        elif bar >= weights[2]:
            bar -= weights[2]
            counts[0] += 1
    if bar == 0:
        return " ".join(list(map(str, counts)))
    return -1


def main():
    bar = int(input())
    print(protein(bar))

if __name__ == "__main__":
    main()
