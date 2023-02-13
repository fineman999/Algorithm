from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = [0]
    before = prices.pop()
    cnt = 1
    queue = deque([before])
    while prices:
        now = prices.pop()
        valid = False
        for i in range(len(queue)):
            if now > queue[i]:
                answer.append(i + 1)
                valid = True
                break
        if not valid:
            queue = deque()
            answer.append(cnt)
        queue.appendleft(now)

        cnt += 1

    return answer[::-1]

def main():
    print(solution([1, 2, 3, 1, 3]	))

if __name__ == "__main__":
    main()
