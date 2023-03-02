from itertools import combinations, permutations, product


def solution(users, emoticons):
    result = []
    discounts = [40, 30, 20, 10]
    n = len(emoticons)

    for dis in product(discounts, repeat=n):
        answer = [0, 0]
        for user in users:
            [user_discount, max_price] = user
            check = 0
            for i in range(n):
                if dis[i] >= user_discount:
                    check += emoticons[i] - int(emoticons[i] * (dis[i] / 100))
            if check >= max_price:
                answer[0] += 1
            else:
                answer[1] += check

        if not result:
            result = answer
        else:
            if result[0] < answer[0]:
                result = answer
            elif result[0] == answer[0] and result[1] < answer[1]:
                result = answer
    return result

def main():
    print(solution([[40, 10000], [25, 10000]],	[7000, 9000]))


if __name__ == "__main__":
    main()