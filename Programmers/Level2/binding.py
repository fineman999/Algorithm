def solution(picks, minerals):
    answer = 0
    temp = []
    tmp = [0, 0, 0]
    n = sum(picks) * 5
    for i in range(len(minerals)):
        if n < i:
            break
        if i != 0 and i % 5 == 0:
            temp.append(tmp)
            tmp = [0, 0, 0]
        if minerals[i] == 'diamond':
            tmp[0] += 1
        if minerals[i] == 'iron':
            tmp[1] += 1
        if minerals[i] == 'stone':
            tmp[2] += 1

    if tmp != [0, 0, 0]:
        temp.append(tmp)
        temp.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for d, i, s, in temp:
        if picks[0] > 0:
            answer += d + i + s
            picks[0] -= 1
        elif picks[1] > 0:
            if d > 0:
                answer += 5 * d
            answer += i + s
            picks[1] -= 1
        elif picks[2] > 0:
            if d > 0:
                answer += 25 * d
            if i > 0:
                answer += 5 * i
            answer += s
            picks[2] -= 1

    return answer

def main():
    solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])

if __name__ == '__main__':
    main()