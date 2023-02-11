from collections import defaultdict
def solution(clothes):
    answer = 1
    close = defaultdict(list)
    for name, types in clothes:
        close[types].append(name)

    for value in close.values():
        answer *= (len(value) + 1)

    return answer - 1


def main():
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],["yeow_hat", "headgear"],["yellow_hat", "headar"]]))

if __name__ == "__main__":
    main()