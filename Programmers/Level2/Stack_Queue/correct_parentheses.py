def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] == "(":
            answer.append(1)
        else:
            try:
                answer_pop = answer.pop()
                if not answer_pop:
                    return False
            except:
                return False
    if answer:
        return False
    return True


def main():
    s = input()
    print(solution(s))


if __name__ == "__main__":
    main()
