import itertools
def checkDecimal(num):
    check = False
    for i in range(2,num):
        if num%i == 0:
            check = True
            break
    return check


def solution(nums):
    combinations = itertools.combinations(nums, 3)
    cnt = 0
    for combination in combinations:
        i = sum(combination)
        if not checkDecimal(i):
            cnt += 1
    return cnt


def main():
    print(solution([1,2,3,4]))


if __name__ == "__main__":
    main()
