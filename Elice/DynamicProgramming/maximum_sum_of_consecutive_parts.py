def getSubsum(data) :
    '''
    n개의 숫자가 list로 주어질 때, 그 연속 부분 최대합을 반환하는 함수를 작성하세요.
    f(n) = max(f(n-1), 0) + data[n]
    '''

    answer = []
    max_answer = -100_100_100
    answer.append(data[0])
    for i in range(1,len(data)):
        element = max(answer[i-1], 0) + data[i]
        answer.append(element)
        max_answer = max(element, max_answer)
    return max_answer


def main():

    arr = list(map(int, input().split()))
    return print(getSubsum(arr))


if __name__ == "__main__":
    main()
