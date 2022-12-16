def solution(a, b, n):
    answer_bottle = 0
    remain_bottle = 0
    while n >= a:
        answer = (n//a)*b
        remain_bottle += n % a

        answer_bottle += answer
        while answer %a != 0:
            remain_bottle -= 1
            if remain_bottle == -1:
                remain_bottle = 0
                break
            answer +=1
        n = answer
    if remain_bottle > 0:
        answer_bottle += remain_bottle
    return answer_bottle

def main():
    print(solution(2, 1, 20))


if __name__ == "__main__":
    main()
