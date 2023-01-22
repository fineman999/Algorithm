

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1],-x[0]))
    answer = 0
    for i in range(row_begin-1,row_end):
        answer_sum = 0
        for j in range(len(data[i])):
            answer_sum += data[i][j]%(i+1)
        if answer == 0:
            answer = answer_sum
        else:
            answer = answer_sum ^ answer

    return answer


def main():
    print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))


if __name__ == "__main__":
    main()