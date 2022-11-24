def LIS(myData) :
    '''
    수열이 list로 주어질 때, 최장 증가 부분 수열의 길이를 반환하는 함수를 작성하세요.
    '''
    arr = [0]*len(myData)
    arr[0] = 1
    for i in range(1,len(myData)):
        for j in range(i):
            if myData[j] < myData[i]:
                arr[i] = max(arr[j]+1, arr[i])

    return max(arr)



def main():

    arr = list(map(int, input().split()))
    print(LIS(arr))

if __name__ == "__main__":
    main()