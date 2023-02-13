def solution(brown, yellow):
    answer = []
    arr = []
    sizes = brown + yellow
    for i in range(sizes, 1, -1):
        if sizes%i == 0:
            get_yellow = sizes//i
            if brown == i*2 + (get_yellow - 2)*2:
                return [i, get_yellow]
        arr.append(i)
    return answer


def main():
    print(solution(10,2))


if __name__ == "__main__":
    main()
