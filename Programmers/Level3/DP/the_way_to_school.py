
def solution(m, n, puddles):
    answer = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            valid = False
            for puddle in puddles:
                if j == puddle[0] - 1 and i == puddle[1] - 1:
                    puddles.remove(puddle)
                    valid = True
                    continue
            if valid:
                continue
            if i == 0 and j == 0:
                answer[i][j] = 1
            elif i == 0:
                answer[i][j] += answer[i][j-1]
            elif j == 0:
                answer[i][j] += answer[i-1][j]
            else:
                answer[i][j] = answer[i-1][j] + answer[i][j-1]
    return answer[-1][-1]%1_000_000_007


def main():
    print(solution(4, 3,	[[2, 2]]))


if __name__ == "__main__":
    main()
