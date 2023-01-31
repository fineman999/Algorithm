parents = []

# 부모 원소 찾기
def find_set(x):
    while x != parents[x]:
        x = parents[x]
    return x

# n: node
def solution(n, costs):
    global parents
    answer = 0
    # 정렬
    costs.sort(key=lambda x: x[2])

    # 부모
    parents = [x for x in range(n)]
    distance, cnt = 0, 0

    for start, end, value in costs:
        # 해당 간선이 사이클을 만들지 않는다면
        if find_set(start) != find_set(end):
            # union 연산 수행, (end의 대표 원소가 start의 대표 원소를 가르키게 한다.)
            parents[find_set(end)] = find_set(start)
            distance += value
            cnt += 1
            if cnt > n:
                break

    return distance


def main():
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))


if __name__ == "__main__":
    main()
