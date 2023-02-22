

def solution(s, skip, index):
    alphabets = [chr(i) for i in range(97, 123)]

    skip = set(skip)
    alphabets = set(alphabets)
    alphabets -= skip

    alphabets = sorted(alphabets)
    length  = len(alphabets)
    answer = ""
    diary = {alpha: idx for idx, alpha in enumerate(alphabets)}
    for i in range(len(s)):
        answer += alphabets[(diary[s[i]] + index)%length]

    return answer

def main():
    print(solution(	"aukks", "wbqd", 5))

if __name__ == "__main__":
    main()