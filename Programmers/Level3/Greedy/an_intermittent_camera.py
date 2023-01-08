def solution(routes):
    routes.sort(key=lambda x:x[1])

    answer = 0
    check = [0,0]

    for route in routes:
        [start, end] = route
        if check == [0,0]:
            check = [start, end]
            answer += 1
        else:
            valid = False
            for i in range(check[0], check[1]+1):
                if start <= i <= end:
                    valid = True
                    break
            if not valid:
                check = [start, end]
                answer += 1
    return answer


def main():
    print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]]))


if __name__ == "__main__":
    main()