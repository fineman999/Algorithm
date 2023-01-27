from collections import deque
def solution(gems):
    answer = [0,100_001]
    n = len(set(gems))
    result = []
    dictionary = dict()
    start = 0
    end = 0
    while start <= end and end < len(gems):
        if gems[end] not in dictionary:
            dictionary[gems[end]] = 1
        else:
            dictionary[gems[end]] += 1

        if len(dictionary.keys()) == n:
                while start <= end:
                    if len(dictionary.keys()) == n:
                        result.append([start+1,end+1])
                        if answer[1]- answer[0] > end-start:
                            answer = [start+1,end+1]
                    else:
                        break
                    dictionary[gems[start]] -= 1
                    if dictionary[gems[start]] == 0:
                        del dictionary[gems[start]]
                    start += 1
        end += 1
    return answer

def main():
    print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))


if __name__ == "__main__":
    main()