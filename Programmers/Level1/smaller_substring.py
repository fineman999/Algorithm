def solution(t, p):
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        if int(p) >= int(t[i:i+len(p)]):
            # print(int(t[i:i+len(p)]))
            answer += 1
    return answer
def main():
    print(solution("10203", "15"))


if __name__ == "__main__":
    main()

