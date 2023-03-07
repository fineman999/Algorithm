import math
import sys
N = 10_001
numbers = [True]*N
def check_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if numbers[i]:
            j = 2
            while i*j < N:
                numbers[i*j] = False
                j += 1


def solution(number):

    answer = [0,math.inf]
    start = number-1
    for i in range(start, number//2-1, -1):
        if numbers[i] and numbers[number-i]:
            if abs(answer[0]-answer[1]) > abs(2*i - number):
                answer = [number-i, i]
    return answer


def main():
    T = int(sys.stdin.readline().rstrip())
    check_prime(N)
    answer = []
    for i in range(T):
        arr = int(sys.stdin.readline().rstrip())
        answer.append(solution(arr))
    for i in answer:
        print(f"{i[0]} {i[1]}")



if __name__ == "__main__":
    main()