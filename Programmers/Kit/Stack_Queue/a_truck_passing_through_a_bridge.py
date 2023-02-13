from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = len(truck_weights)
    truck_weights = deque(truck_weights)
    timer = deque()
    working = deque()
    finished = []
    while len(finished) < n:

        for i in range(len(timer)):
            timer[i] += 1
        while timer:
            if timer[0] == bridge_length:
                timer.popleft()
                finished.append(working.popleft())
            else:
                break
        if truck_weights:
            if sum(working) + truck_weights[0] <= weight:
                working.append(truck_weights.popleft())
                timer.append(0)
        answer += 1
    return answer

def main():
    print(solution(2, 10, [7, 4, 5, 6]))

if __name__ == "__main__":
    main()
