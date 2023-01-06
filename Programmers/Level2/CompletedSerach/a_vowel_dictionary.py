import itertools

dict = ['A','E','I','O','U']
def solution(word):

    answer = []
    cnt = 1
    for j in range(1, 6):
        for i in itertools.product(dict, repeat=j):
            answer.append("".join(i))
    answer.sort()
    for i in answer:
        if i == word:
            break
        cnt += 1
    return cnt



def main():
    print(solution("AAAAE"))


if __name__ == "__main__":
    main()