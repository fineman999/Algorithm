import itertools

def permutations(arr, n):
    ret = []
    if n == 1:
        for i in arr:
            ret.append(str(i))
    else:
        for i in range(len(arr)):
            for p in permutations(arr, n-1):
                ret.append(str(arr[i])+" "+str(p))
    return ret


def calculate(n, m):
    arr = [i for i in range(1,n+1)]
    return permutations(arr, m)



def main():
    n, m = map(int, input().split())
    result = calculate(n, m)
    for arr in result:
        print(arr)


if __name__ == "__main__":
    main()