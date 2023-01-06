
import collections
def solution(want, number, discount):
    n = len(discount)
    cnt = 0
    for i in range(len(discount)):
        if i + 10 > n:
            break
        items = collections.Counter(discount[i:i + 10])
        valid = True

        for j in range(len(want)):
            if want[j] not in items:
                valid = False
                break
            if items.get(want[j]) != number[j]:
                valid = False
                break
        if valid:
            cnt += 1
    return cnt



def main():
    print(solution(["banana", "apple", "rice", "pork", "pot"],
                   [3, 2, 2, 2, 1],
                   ["chicken", "apple", "apple", "banana", "rice", "apple",
                    "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))


if __name__ == "__main__":
    main()