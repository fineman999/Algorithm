def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            ele = 0
            for k in range(len(arr1[0])):
                ele += arr1[i][k] * arr2[k][j]
            row.append(ele)
        answer.append(row)
    return answer


def main():
    print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))


if __name__ == "__main__":
    main()
