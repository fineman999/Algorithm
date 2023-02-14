
result = 0
cnt = 0


def dfs(vowel, word, n):
    if len(n) == 5:
        return

    for i in range(len(vowel)):
        new_word = n + vowel[i]
        global cnt
        cnt += 1
        if word == new_word:
            global result
            result = cnt
            return 1
        dfs(vowel, word, new_word)


def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    dfs(vowel, word, "")
    return result

def main():
    print(solution("AAAAE"))


if __name__ == "__main__":
    main()
