#
def recursive(arr,n,k):
    result = 0
    if n == k:
        return 1
    else:
        for i in range(n):
            if i in arr:
                continue
            valid = True
            for j in range(len(arr)-1,-1,-1):
                if abs(arr[j]-i) == abs(len(arr)-j):
                    valid = False
                    break
            if valid:
                arr.append(i)
                result += recursive(arr,n,k+1)
                arr.remove(i)
        return result


def solution(n):
    answer = 0
    arr = []

    for i in range(n):
        arr.append(i)
        answer += recursive(arr, n, 1)
        arr = []
    return answer


def main():
    print(solution(4))


if __name__ == "__main__":
    main()