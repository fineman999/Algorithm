from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)
    dp[1].add(N)
    for i in range(2, 10):
        dp[i].add(N**i)

    for i in range(1, 10):
        for j in range(1, 10):
            if i + j > 9:
                continue
            for h in dp[i]:
                for u in dp[j]:
                    dp[i + j].add(h * u)
                    if h - u > 0:
                        dp[i + j].add(h - u)
                    if u > 0:
                        dp[i + j].add(h // u)
                    dp[i + j].add(h + u)
                    if all(str(N) == cha for cha in list(map(str, str(h)))) \
                            and all(str(N) == cha for cha in list(map(str, str(u)))):
                        dp[i+j].add(int(str(h)+str(u)))

    for i in range(1, 10):
        if number in dp[i]:
            return i
    return -1

def main():
    print(solution(8,	5800))


if __name__ == "__main__":
    main()
