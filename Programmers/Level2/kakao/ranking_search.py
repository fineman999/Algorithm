
from bisect import bisect_left
dictionary = dict()
# def binary_search(score: int, information: list, start: int, end: int)-> int:
#     result = (start+end)//2
#     if start >= end:
#         return 0
#
#     if information[result] == score:
#         return result
#     elif information[result] > score:
#         return binary_search(score,information, start,result-1)
#     else:
#         return binary_search(score, information, result+1,end)


def dfs(info: list, cnt: int, result: str):
    if cnt == 4:
        if result not in dictionary:
            dictionary[result] = [int(info[-1])]
        else:
            dictionary[result].append(int(info[-1]))
    else:
        dfs(info, cnt+1, result+info[cnt])
        dfs(info, cnt+1,result+"-")

def solution(info, query):
    answer = []
    global dictionary
    for i in info:
        dfs(i.split(),0,"")

    for key,value in dictionary.items():
        value.sort()

    for que in query:
        que_split = que.split()
        start = [que_split[0], que_split[2], que_split[4], que_split[6]]
        score = int(que_split[7])
        check = "".join(start)
        try:
            scores = dictionary[check]
            n = len(scores)
            index = bisect_left(scores, score)
            cnt = n - index
            answer.append(cnt)
        except:
            answer.append(0)

    return answer


def main():
    print(solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))


if __name__ == "__main__":
    main()