def solution(s):
    rotates = list(s)
    answer = [rotates.pop(0)]
    cnt = 0
    while rotates:
        rotate_pop = rotates.pop(0)
        try:
            answer_pop = answer.pop()
            valid = True
            if answer_pop == "(" and rotate_pop == ")":
               cnt += 1
               valid = False
            elif answer_pop == "{" and rotate_pop == "}":
               cnt += 1
               valid = False
            elif answer_pop == "[" and rotate_pop == "]":
               cnt += 1
               valid = False

            if valid:
                answer.append(answer_pop)
                answer.append(rotate_pop)
        except:
            answer.append(rotate_pop)

    return cnt


def main():
    print(solution("}]()[{"))


if __name__ == "__main__":
    main()
