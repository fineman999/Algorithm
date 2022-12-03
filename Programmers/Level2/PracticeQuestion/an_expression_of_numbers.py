def solution(n):
    answer = 0
    result = 0
    for i in range(1, n+1):
        result += i
        if result == n:
            answer += 1
        elif result > n:
            result = 0
            for j in range(i,-1,-1):
                result += j
                if result == n:
                    answer += 1
                elif result > n:
                    result -= j
                    break

    return answer

def main():
    s = int(input())
    print(solution(s))


if __name__ == "__main__":
    main()
