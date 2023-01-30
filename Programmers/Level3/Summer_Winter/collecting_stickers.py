def calculator(sticker):
    if sticker[0] > sticker[1]:
        dp = [sticker[0], sticker[0]]
    else:
        dp = [sticker[0], sticker[1]]
    for i in range(2,len(sticker)):
        dp.append(max(dp[i-1], dp[i-2]+sticker[i]))
    # print(dp)
    return dp[-1]


def solution(sticker):

    if len(sticker) < 4:
        return max(sticker)

    sticker_a = sticker[:-1]
    sticker_b = sticker[1:]
    answer = max(calculator(sticker_a), calculator(sticker_b))

    return answer

def main():
    print(solution([14, 24, 5, 11, 20]))


if __name__ == "__main__":
    main()
