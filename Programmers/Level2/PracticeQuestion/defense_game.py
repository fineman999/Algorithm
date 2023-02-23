import heapq
def solution(n, k, enemy):
    answer = 0
    q = []
    max_sum = 0
    max_element = 0
    for i in range(len(enemy)):
        max_sum += enemy[i]

        heapq.heappush(q, -enemy[i])
        if max_sum <= n:
            continue
        else:
            if k > 0:
                max_sum += heapq.heappop(q)
                k -= 1
            else:
                answer = i
                break

    if answer == 0:
        return len(enemy)

    return answer

def main():
    # print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
    print(solution(2, 4, [3, 3, 3, 3]))


if __name__ == "__main__":
    main()