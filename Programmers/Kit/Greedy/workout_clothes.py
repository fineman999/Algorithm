def solution(n, lost, reserve):
    arr = [1]*(n+1)

    # 1 ~ n 명 체육복 개수 초기화
    for i in range(len(lost)):
        arr[lost[i]] -= 1
    for i in range(len(reserve)):
        arr[reserve[i]] += 1

    # 빌려주기 계산
    for i in range(1, len(arr)):
        if arr[i] == 0:
            if i - 1 > 0 and arr[i-1] > 1:
                arr[i] += 1
                arr[i-1] -= 1
            elif i + 1 < len(arr) and arr[i+1] > 1:
                arr[i] += 1
                arr[i+1] -= 1

    # 체육복을 가지고 있는 개수 계산
    answer = 0
    for i in range(1, len(arr)):
        if arr[i] > 0:
            answer += 1
    return answer
def main():
    print(solution(5, [2, 4], [3]))


if __name__ == "__main__":
    main()

