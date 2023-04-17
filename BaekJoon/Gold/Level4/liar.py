import sys


def add_truth_know_people(parties, truth):
    # 어떤 사람이 어떤 파티에서는 진실을 듣고,
    # 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 되는 경우의 수를 모두 구하려면
    # 모든 파티 인원을 반복해야 됨
    for _ in range(len(parties)):
        for party in parties:
            if party & truth:
                truth = party | truth
    return truth


def check_truth_know_people(parties, truth):
    answer = 0
    for party in parties:
        if not party & truth:
            answer += 1
    return answer


def solution(truth, parties):
    truth = add_truth_know_people(parties, truth)
    answer = check_truth_know_people(parties, truth)
    return answer


def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    truth = set(temp[1:])
    parties = []
    for _ in range(M):
        check = list(map(int, sys.stdin.readline().rstrip().split()))

        parties.append(set(check[1:]))
    print(solution(truth, parties))


if __name__ == '__main__':
    main()
