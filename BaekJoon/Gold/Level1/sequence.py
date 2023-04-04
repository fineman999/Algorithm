import sys
from itertools import combinations
import bisect
from collections import defaultdict
# meet_in_the middle 알고리즘
def get_sub_seq(left_seq, left_n, S):
    sub = set()
    cnt = 0
    diary = defaultdict(int)
    # print(left_seq, left_n)
    for num in range(1, left_n+1):
        # print(num,"num")
        for sub_set in combinations(left_seq, num):
            # print(sub_set)
            sum_sub = sum(sub_set)
            if sum_sub == S:
                cnt +=1
            sub.add(sum_sub)
            diary[sum_sub] += 1
    return sub, cnt, diary

def meet_in_the_middle(N, S, seq):

    mid = N//2

    # 1. 둘로 나누기
    left_seq = seq[:mid]
    right_seq = seq[mid:]

    cnt = 0
    # 2. 길이 구하기
    left_n = len(left_seq)
    right_n= len(right_seq)


    # 3. 왼쪽 순열과 오른쪽 순열 구하기
    left_sub, left_cnt, left_diary = get_sub_seq(left_seq, left_n, S)
    right_sub, right_cnt, right_diary = get_sub_seq(right_seq, right_n, S)

    cnt += left_cnt + right_cnt
    # 4. 오른쪽 순열 정렬 -> 이진 탐색을 위해
    right_sub = list(right_sub)
    right_sub.sort()
    right_sub_n = len(right_sub)
    # 4. 이진탐색
    for element in left_sub:
        check = S - element
        tmp = bisect.bisect_left(right_sub, check)
        if tmp < right_sub_n and S == element + right_sub[tmp]:
            cnt += left_diary[element]*right_diary[right_sub[tmp]]
    return cnt

        # 이분 탐색




def solution(N, S, seq):
    count = meet_in_the_middle(N, S, seq)

    return count


def main():
    N, S = map(int, sys.stdin.readline().split())
    seq = list(map(int, sys.stdin.readline().split()))
    answer = solution(N, S, seq)
    print(answer)


if __name__ == "__main__":
    main()
