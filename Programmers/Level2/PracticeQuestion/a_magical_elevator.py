from collections import deque
def dfs(queue, cnt):
    if not queue:
        return [cnt]
    answer = []
    pop = queue.pop()
    if pop == 10:
        if not queue:
            answer += dfs(queue,cnt+1)
        else:
            change = queue.pop()
            change += 1
            queue.append(change)
            answer += dfs(queue,cnt)
    else:
        # 깊은 복사라서 새로운 큐를 생성해서 따로 생성하기
        new_queue = deque(list(queue))
        right = 10-pop
        left = pop
        answer += dfs(queue, left + cnt)
        new_queue.append(10)
        answer += dfs(new_queue, right + cnt)

    return answer

def solution(storey):
    arr = list(map(int,str(storey)))
    queue = deque(arr)

    return min(dfs(queue,0))


def main():
    print(solution(16))


if __name__ == "__main__":
    main()