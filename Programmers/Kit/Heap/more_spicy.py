import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) > 1 and any(K > element for element in scoville):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    if not any(K > element for element in scoville):
        return answer
    return -1

def main():
    print(solution([1, 2, 3, 9, 10, 12], 7))

if __name__ == "__main__":
    main()
