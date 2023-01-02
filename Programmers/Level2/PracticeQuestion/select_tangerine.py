from collections import deque
def solution(k, tangerine):
    dictionary= dict()
    for i in range(len(tangerine)):
        if tangerine[i] not in dictionary:
            dictionary[tangerine[i]] = 1
        else:
            dictionary[tangerine[i]] += 1
    arr = []
    for key, value in dictionary.items():
        arr.append([key,value])
    arr.sort(key=lambda x: x[1])
    queue = deque(arr)
    if k > len(tangerine)//2:
        n = len(tangerine) - k
        while queue:
            queue_pop = queue.popleft()
            n -= queue_pop[1]
            if n < 0:
                return len(queue) + 1
            elif n == 0:
                return len(queue)
        return 0
    n = k
    send_queue = deque()
    while queue:
        queue_pop = queue.pop()
        n -= queue_pop[1]
        send_queue.append(queue_pop)
        if n == 0:
            return len(send_queue)
        elif n < 0:
            return len(send_queue)
    return len(send_queue)



def main():
    print(solution(	2, [1, 1, 1, 1, 2, 2, 2, 3]))


if __name__ == "__main__":
    main()
