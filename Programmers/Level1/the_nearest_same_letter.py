def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            answer.append(i - s[:i].rindex(s[i]))
    return answer


def main():
    print(solution("banana"))


if __name__ == "__main__":
    main()