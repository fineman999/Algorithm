import itertools


def combinations(arr, n):
    return itertools.combinations(arr,n)


def calculate(n, m):
    arr = [i for i in range(1,n+1)]
    return combinations(arr, m)


def main():
    n, m = map(int, input().split())
    result = calculate(n, m)
    for arr in result:
        print(" ".join(list(map(str, arr))))


if __name__ == "__main__":
    main()