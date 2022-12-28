from collections import deque

def solution(msg):
    dictionary = dict()
    for i in range(0, 26):
        dictionary[chr(65+i)] = i+1
    last_number = 27
    answer = []
    msg = deque(msg)
    msg_w = ""
    msg_output = 0
    while msg:
        msg_w += msg.popleft()
        if msg_w not in dictionary:
            msg_output = dictionary[msg_w[:-1]]
            answer.append(msg_output)
            dictionary[msg_w] = last_number
            last_number += 1
            msg_w = msg_w[-1]
    if msg_w in dictionary:
        answer.append(dictionary[msg_w])
    return answer


def main():
    print(solution("TOBEORNOTTOBEORTOBEORNOT"))


if __name__ == "__main__":
    main()
