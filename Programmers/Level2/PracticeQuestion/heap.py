import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    check = True
    cnt = 0
    while check:
        check = False
        if scoville[0] < K:
            check = True
            try:
                first = heapq.heappop(scoville)
                second = heapq.heappop(scoville)
                new_scov = first + second*2
                heapq.heappush(scoville, new_scov)
            except:
                return -1
            cnt += 1

    return cnt


def main():
    print(solution([1, 2, 3, 9, 10, 12], 7))


if __name__ == "__main__":
    main()
