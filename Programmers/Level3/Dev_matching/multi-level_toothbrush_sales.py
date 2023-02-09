from collections import defaultdict
import math

dictionary = defaultdict(str)
people = defaultdict(int)


def find_parent(x: str, money: int):
    global dictionary
    global people
    while x != dictionary[x]:
        if money == 0:
            break
        mine = math.ceil(money*0.9)
        money = money - mine
        people[x] += mine
        x = dictionary[x]


def check_amount(seller: list, amount: list):
    global people
    for i in range(len(seller)):
        find_parent(seller[i], amount[i]*100)


def solution(enroll, referral, seller, amount):

    global dictionary
    global people
    dictionary['-'] = '-'
    for i in range(len(enroll)):
        dictionary[enroll[i]] = referral[i]
        people[enroll[i]] = 0

    check_amount(seller, amount)
    return list(people.values())


def main():
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))


if __name__ == "__main__":
    main()