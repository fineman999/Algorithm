
def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    answer = 0
    for element in babbling:
        for j in arr:
            if j*2 not in element:
                element = element.replace(j, " ")

        if len(element.strip(" ")) == 0:
            answer += 1
    return answer


def main():
    print(solution(	["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))


if __name__ == "__main__":
    main()