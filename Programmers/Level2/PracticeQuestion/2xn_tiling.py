

def solution(n):
    answer = []
    answer.append(0)
    answer.append(1)
    answer.append(2)
    for i in range(3,n+1):
        answer.append(answer[i-1] + answer[i-2])

    return answer[-1]%1_000_000_007



def main():
    print(solution(4))


if __name__ == "__main__":
    main()