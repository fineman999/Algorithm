def cutRod(N, myData) :
    '''
    통나무의 길이 N과 가격표가 dictionary로 주어질 때, 통나무를 잘라서 얻을 수 있는 최대 이익을 반환하세요.
    예) 길이 1의 가격이 3일 때, myData[1] = 3
    max_myData[i] = max(max_myData[n-i] + myData[i] for 0 ~ n)
    '''

    max_myData = [0 for i in range(N+1)]

    for i in range(N+1):
        for l, p in myData.items():
            if i >= l:
                max_myData[i] = max(max_myData[i], max_myData[i-l] + p)

    return max_myData[-1]


def main():
    N, M = map(int, input().split())
    arr = {}
    for i in range(M):
        l, p = list(map(int, input().split()))
        arr[l] = p
    print(cutRod(N, arr))


if __name__ == "__main__":
    main()