def change(x):
    if x == 1 or x == 0:
        return str(x)
    result = x//2
    remainder = x%2
    return str(change(result))+str(remainder)

def solution(s):
    answer = [0,0]
    while True:
        if s == "1":
            break
        zero = s.count("0")
        x = len(s) - zero
        s = change(x)
        answer[0] += 1
        answer[1] += zero
    return answer

def main():
    s = input()
    print(solution(s))
    # print(change(4))

if __name__ == "__main__":
    main()
