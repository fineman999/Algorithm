import sys
from collections import defaultdict
def find_parents(hash_friends, friend):
    start = friend
    while hash_friends[friend] != friend:
        friend = hash_friends[friend]
    hash_friends[start] = friend
    return friend


def solution(N, friends):
    # print(friends)
    tmp = set()
    for A, B in friends:
        tmp.add(A)
        tmp.add(B)

    hash_friends = {value: value for value in tmp}
    hash_cnt = {value: 1 for value in tmp}
    answer = []
    for A, B in friends:
        if find_parents(hash_friends, A) != find_parents(hash_friends, B):
            check_b = hash_cnt[find_parents(hash_friends, B)]
            hash_cnt[find_parents(hash_friends, A)] += check_b
            answer.append(hash_cnt[find_parents(hash_friends, A)])
            hash_friends[find_parents(hash_friends, B)] = find_parents(hash_friends, A)
        else:
            answer.append(hash_cnt[find_parents(hash_friends, A)])

    for ele in answer:
        print(ele)


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        friends = []
        for _ in range(N):
            friends.append(list(sys.stdin.readline().rstrip().split()))
        solution(N, friends)

if __name__ == '__main__':
    main()