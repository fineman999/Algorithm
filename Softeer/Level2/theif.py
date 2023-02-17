import sys
from collections import deque
def solution(W, N, bags):
    bags.sort(key = lambda x:x[1], reverse = True)
    q = deque(bags)
    answer = 0
    while q:
        [weight, price] = q.popleft()
        if W == 0:
            break
        if W >= weight:
            answer += weight*price
            W -= weight
        elif W < weight:
            answer += W*price
            W = 0
    return answer

def main():
    W, N = map(int, sys.stdin.readline().split())
    bags = []
    for i in range(N):
        bags.append(list(map(int, sys.stdin.readline().split())))

    print(solution(W, N, bags))

if __name__ == "__main__":
    main()