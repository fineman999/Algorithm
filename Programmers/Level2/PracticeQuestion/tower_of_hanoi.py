
def recursive(n, first, destination, second, arr):
    if n == 1:
        arr.append([first,destination])
        # print(first,"->",destination)
        return
    recursive(n-1,first, second, destination, arr)
    arr.append([first, destination])
    # print(first,"->",destination)
    recursive(n-1,second,destination,first, arr)
    return arr


def solution(n):
    answer = []
    answer = recursive(n, 1,3,2, answer)
    return answer


def main():

    return print(solution(2))


if __name__ == "__main__":
    main()
