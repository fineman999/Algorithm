def solution(n):


    answer = [0,1,2]
    if n < 3:
        return answer[n]
    for i in range(3, n+1):
        answer.append(answer[i-1] + answer[i-2])

    return answer[-1]%1234567




def main():

    print(solution(1))


if __name__ == "__main__":
    main()
