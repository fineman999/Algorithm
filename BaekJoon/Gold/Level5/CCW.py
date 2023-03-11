import sys

def ccw(arr):
    [x1,y1] = arr[0]
    [x2,y2] = arr[1]
    [x3, y3] = arr[2]
    return (x1*y2 + x2*y3 + x3*y1) - (y1*x2+y2*x3+y3*x1)


def solution(arr):
    check = ccw(arr)
    if check < 0:
        return -1
    elif check > 0:
        return 1
    return 0





def main():
    arr = []
    for i in range(3):
        arr.append(list(map(int,sys.stdin.readline().rstrip().split())))
    print(solution(arr))

if __name__ == '__main__':
    main()