from collections import deque
def dfs(now, dungeons, cnt):
    if not dungeons:
        return cnt
    get_cnt = cnt
    for dungeon in dungeons:
        [smaller, discount] = dungeon
        if now >= smaller:
            new_now = now
            new_now -= discount
            new_dungeons = [ele for ele in dungeons]
            new_dungeons.remove(dungeon)
            get_cnt = max(get_cnt, dfs(new_now, new_dungeons, cnt + 1))
    return get_cnt

def solution(k, dungeons):

    answer = dfs(k, dungeons, 0)

    return answer

def main():
    print(solution(80, [[80,20],[50,40],[30,10]]))


if __name__ == "__main__":
    main()
