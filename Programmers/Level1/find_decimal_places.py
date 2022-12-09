import math

def solution(n):

    answer = [True]*(n+1)

    for i in range(2, n+1):
        if answer[i] == True:
            for j in range(2,n+1):
                if i*j > n:
                    break
                answer[i*j] = False

    return answer[2:].count(True)



def main():
    print(solution(5))


if __name__ == "__main__":
    main()
