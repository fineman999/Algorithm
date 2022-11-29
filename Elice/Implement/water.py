def water(bottles, lids):
    return min(bottles)+min(lids) + 10

def main():
    bottles = []
    lids = []
    for _ in range(3):
        bottles.append(int(input()))
    for _ in range(2):
        lids.append(int(input()))
    print(water(bottles, lids))

if __name__ == "__main__":
    main()