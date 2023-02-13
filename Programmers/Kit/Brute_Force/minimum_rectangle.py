
def solution(sizes):
    answer = [0,0]
    for left, right in sizes:
        if left < right:
            left, right = right, left
        answer[0] = max(answer[0],left)
        answer[1] = max(answer[1],right)

    return answer[0]*answer[1]


def main():
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))


if __name__ == "__main__":
    main()
