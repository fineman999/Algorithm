import copy


def dfs(dungeons: list, k: int, cnt):
    answer_cnt = cnt
    for dungeon in dungeons:
        [need_fatigue, decrease_fatigue] = dungeon
        if k >= need_fatigue:
            new_dungeons = copy.deepcopy(dungeons)
            new_dungeons.remove(dungeon)
            answer_cnt = max(dfs(new_dungeons, k - decrease_fatigue, cnt + 1), answer_cnt)
    return answer_cnt


def solution(k, dungeons):
    answer = dfs(dungeons, k, 0)
    return answer

def main():
    print(solution(	80, [[80, 20], [50, 40], [30, 10]]))


if __name__ == "__main__":
    main()
