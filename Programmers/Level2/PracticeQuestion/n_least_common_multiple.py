def GCD(x,y):
    while y:
        x, y= y, x%y
    return x

def multiple(x,y):
    return x*y // GCD(x,y)

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    start = multiple(arr[0],arr[1])
    for i in range(2, len(arr)):
        start = multiple(start, arr[i])

    return start



def main():

    print(solution([2,6,8,14]))


if __name__ == "__main__":
    main()
