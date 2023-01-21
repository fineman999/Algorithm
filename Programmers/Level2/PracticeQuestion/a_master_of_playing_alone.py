def recursive(new_cards: list, visited: list, i: int,cnt: int) -> list:
    result = []
    if visited[i]:
        return [cnt]
    visited[i] = True
    get_cnt = recursive(new_cards,visited,new_cards[i], cnt + 1)
    result += get_cnt
    for i in range(len(visited)):
        if not visited[i]:
            new_visited = visited
            result += recursive(new_cards,new_visited,i,0)
    return result


def solution(cards):
    # 계산 편리하게 의미 없는 0 값 넣기
    cards.insert(0,0)

    new_cards = cards
    visited = [False] * (len(cards))
    visited[0] = True
    get_result = recursive(new_cards, visited, 1, 0)
    if len(get_result) <= 1:
        return 0
    get_result.sort(reverse=True)
    return get_result[0]*get_result[1]

def main():
    print(solution([8,6,3,7,2,5,1,4]))


if __name__ == "__main__":
    main()