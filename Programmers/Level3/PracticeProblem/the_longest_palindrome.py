

def check_one(i, s, cnt):
    for j in range(1,len(s)):
        if i - j > -1 and i + j < len(s):
            # print(i-j, i+j)
            if s[i - j] == s[i + j]:
                cnt += 2
            else:
                break
        else:
            break
    return cnt


def check_double(i, s, cnt):
    for j in range(len(s)):
        if i - j > -1 and i + j + 1 < len(s):
            if s[i - j] == s[i + j + 1]:
                cnt += 2
            else:
                break
        else:
            break
    return cnt


def solution(s):
    n = len(s)
    max_cnt = 0
    for i in range(n):
        max_cnt = max(check_one(i, s, 1), max_cnt, check_double(i, s, 0))
    return max_cnt


def main():
    print(solution("abccbaba"))

if __name__ == "__main__":
    main()