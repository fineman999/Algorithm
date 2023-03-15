import sys


def check_palin(arr, i, N):
    left = i - 1
    right = i + 1
    cnt = 0
    while left > -1 and right < N:
        if arr[left] == arr[right]:
            cnt += 2
        else:
            break
        left -= 1
        right += 1
    return cnt


def check_palin_two(arr, i, N):
    left = i
    right = i + 1
    cnt = 0
    while left > -1 and right < N:
        if arr[left] == arr[right]:
            cnt += 2
        else:
            break
        left -= 1
        right += 1
    return cnt


def solution(N, M, arr, questions):
    dp = [1]*(N+1)
    dp_two = [0]*(N+1)
    dp[0] = 0
    for i in range(N):
        cnt = check_palin(arr, i, N)
        cnt_two = check_palin_two(arr, i, N)
        dp_two[i+1] = cnt_two
        dp[i+1] += cnt
    answer = []
    # print(dp_two)
    # print(dp)
    for start, end in questions:
        if arr[start-1] != arr[end-1]:
            answer.append(0)
            continue
        mid = (start + end)//2
        check = (end - start) + 1
        # print(mid, dp[mid],check)
        if check%2==1 and dp[mid] >= check:
            answer.append(1)
        elif check%2 == 0 and dp_two[mid] >= check:
            answer.append(1)
        else:
            answer.append(0)
    return answer



def main():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    questions = []
    M = int(sys.stdin.readline())
    for _ in range(M):
        questions.append(list(map(int, sys.stdin.readline().rstrip().split())))

    answer = solution(N, M, arr, questions)
    for ele in answer:
        print(ele)

if __name__ == '__main__':
    main()