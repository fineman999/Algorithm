

def solution(array, commands):

    answer = []
    for start, end, index in commands:
        arr = array[start-1:end]
        answer.append(sorted(arr)[index-1])
    return answer


def main():
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))


if __name__ == "__main__":
    main()