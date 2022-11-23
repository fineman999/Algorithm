def eating(data) :
    '''
    각 날짜 별 음식의 선호도가 list로 주어질 때, 상훈이가 얻을 수 있는 선호도 총합의 최댓값을 반환하는 함수를 작성하세요.
    answer[i][j] = max(answer[i-1])
    '''
    answer = []
    answer.append(data[0])
    for i in range(1,len(data)):
        answer_init = []
        for j in range(len(data[0])):
            answer_max = 0
            for k in range(len(data[0])):
                if j != k:
                    answer_max = max(answer[i-1][k], answer_max)
            answer_init.append(answer_max + data[i][j])
        answer.append(answer_init)
    result = max(answer[-1])
    return result


def main():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    print(eating(arr))

if __name__ == "__main__":
    main()