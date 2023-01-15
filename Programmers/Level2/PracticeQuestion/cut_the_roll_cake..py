from collections import deque

def solution(topping):


    topping = deque(topping)
    check_a = set()
    cnt = 0
    dictionary = dict()
    for i in topping:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1

    while topping:
        a = len(check_a)
        b = len(dictionary)
        if a == b:
            cnt += 1
        elif a>b:
            break
        popleft = topping.pop()
        dictionary[popleft] -= 1
        if dictionary[popleft] == 0:
            dictionary.pop(popleft)
        check_a.add(popleft)
    return cnt


def main():

    return print(solution([1, 2, 1, 3, 1, 4, 1, 2]))


if __name__ == "__main__":
    main()
