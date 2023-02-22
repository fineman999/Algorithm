def solution(s, skip, index):

    answer = ''

    for i in range(len(s)):
        j = 0
        check = ord(s[i])
        while j < index:
            check += 1
            if check > 122:
                check -= 26
            if chr(check) not in skip:
                j += 1

        if check > 122:
            check -= 26
        answer += chr(check)

    return answer

def main():
    print(solution(	"ybcde", "az", 1))

if __name__ == "__main__":
    main()