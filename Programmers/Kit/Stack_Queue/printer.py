from collections import deque,defaultdict

def solution(priorities, location):

    queue = deque()
    dictionary = defaultdict(int)
    for i, priority in enumerate(priorities):
        dictionary[priority] += 1
        queue.append([priority, i])

    cnt = 1
    while queue:
        [priority, index] = queue.popleft()

        if any(priority < key for key in dictionary.keys()):
            queue.append([priority, index])
        else:
            if location == index:
                return cnt
            cnt += 1
            dictionary[priority] -= 1
            if dictionary[priority] == 0:
                del dictionary[priority]
    return cnt

def main():
    print(solution(	[1, 1, 9, 1, 1, 1], 0))

if __name__ == "__main__":
    main()
