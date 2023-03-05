import sys
from collections import deque

def solution(N, M, printers):
    arr = []

    for i in range(len(printers)):
        if i == M:
            arr.append((printers[i], 1))
        else:
            arr.append((printers[i], 0))
    printers.sort(reverse=True)
    k = 0
    q = deque(arr)
    answer = 1
    while q:
        check = q.popleft()
        if printers[k] != check[0]:
            q.append(check)
        else:
            if check[1] == 1:
                return answer

            k += 1
            answer += 1

    return answer

def main():
    T = int(sys.stdin.readline())
    answer = []
    for i in range(T):
        N, M = map(int, sys.stdin.readline().split())
        printers = list(map(int, sys.stdin.readline().split()))
        answer.append(solution(N, M, printers))

    for element in answer:
        print(element)


if __name__ == "__main__":
    main()