from collections import defaultdict
import heapq
import copy
result = []


def dfs(diary, now, arr):
    if not diary:
        global result
        if not result:
            result = arr
        else:
            result = min(arr,result)
        return
    # print(diary)
    for node in diary[now]:
        new_diary = copy.deepcopy(diary)
        new_diary[now].remove(node)
        if not new_diary[now]:
            del new_diary[now]
        dfs(new_diary, node, arr + [node])


def solution(tickets):
    diary = defaultdict(list)
    for start, end in tickets:
        heapq.heappush(diary[start], end)

    arr = ["ICN"]
    dfs(diary, "ICN", arr)
    return result

def main():
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))


if __name__ == "__main__":
    main()