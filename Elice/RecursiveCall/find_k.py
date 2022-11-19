def findKth(myInput, k):
    '''
    매 순간마다 k번째로 작은 원소를 리스트로 반환합니다.
    '''
    answer = []
    data = []
    for ele in myInput:
        data.append(ele)
        if len(data) < k:
            answer.append(-1)
        else:
            data.sort()
            answer.append(data[k-1])
    return answer


def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    n, k = map(int, input().split())
    myInput = list(map(int, input().split()))

    print('정렬 결과: ', findKth(myInput, k))


if __name__ == "__main__":
    main()
