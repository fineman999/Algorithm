def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    while n!=0:

        if works[0] == 0:
            return 0
        check = works[0]
        for i in range(len(works)):
            if n == 0:
                break
            if works[i] == check:
               works[i] -= 1
               n -= 1
            else:
                break

    for work in works:
        answer += work**2
    return answer




def main():
    print(solution(1, [2,1,2]))


if __name__ == "__main__":
    main()