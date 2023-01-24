
def solution(n):
    answer = [0,0,3,0,11]
    for i in range(5,n+1):
        if i%2==1:
            answer.append(0)
        else:
            check = 0
            for i in range(2,len(answer)-2,2):
                check += answer[i]*2
            answer.append((answer[-2]*3+ check + 2)%1_000_000_007)
    return answer[n]


def main():
    print(solution(6))


if __name__ == "__main__":
    main()