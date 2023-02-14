from collections import deque



def solution(routes):
    routes.sort(key=lambda x: x[1])
    routes = deque(routes)
    compare = []
    answer = 0

    while routes:
        popleft = routes.popleft()
        if not compare:
            compare = popleft
            answer += 1
        else:
            if any(popleft[0] <= i <= popleft[1] for i in range(compare[0], compare[1])):
                continue
            else:
                answer += 1
                compare = popleft

    return answer

def main():
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3],[-3,-2],[-2,10],[5,9],[5,7]]))


if __name__ == "__main__":
    main()
