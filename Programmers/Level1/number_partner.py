from collections import Counter
def second_solution(X, Y):
    X = list(map(int,X))
    y= [0]*10
    for i in range(len(Y)):
        y[int(Y[i])] += 1

    answer = [0]*10
    for i in range(len(X)):
        if y[X[i]] > 0:
            answer[(X[i])] += 1
            y[X[i]] -= 1

    result = ""
    for i in range(len(answer)-1,-1,-1):
        if answer[i] > 0:
            if i == 0 and result == "":
                result += str(i)
                continue
            result += str(i)*answer[i]
    if not result:
        return "-1"
    return result

def solution(X, Y):
    counter_x = Counter(X)
    counter_y = Counter(Y)
    answer = ""
    for i in range(9,-1,-1):
        if str(i) in counter_x and str(i) in counter_y:
            print(counter_x[i])
            if i == 0 and answer == "":
                answer = "0"
                continue
            answer += min(counter_x[str(i)],counter_y[str(i)])*str(i)
    if not answer:
        return "-1"
    return answer

def main():
    print(solution("5525", "1255"))


if __name__ == "__main__":
    main()