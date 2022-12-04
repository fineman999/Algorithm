def solution(n, words):
    answer = []
    arr = [words[0]]

    for i in range(1, len(words)):
        if words[i] in arr:
            answer= [len(arr)%n+1, len(arr)//n+1]
            break
        if arr[i-1][-1] != words[i][0]:
            answer= [len(arr)%n+1, len(arr)//n+1]
            break
        arr.append(words[i])
    if not answer:
        return [0,0]
    return answer


def main():
    print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))


if __name__ == "__main__":
    main()
