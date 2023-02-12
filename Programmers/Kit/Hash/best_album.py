from collections import defaultdict
import heapq

def solution(genres, plays):
    total_plays = defaultdict(int)
    genre_numbers = defaultdict(list)
    for i in range(len(genres)):
        total_plays[genres[i]] += plays[i]
        heapq.heappush(genre_numbers[genres[i]], [-plays[i], i])
    translate_total_plays = []
    for key,value in total_plays.items():
        translate_total_plays.append([value, key])
    translate_total_plays.sort(reverse= True)

    answer = []
    for value, key in translate_total_plays:
        cnt = 0
        while genre_numbers[key]:
            if cnt == 2:
                break
            answer.append(heapq.heappop(genre_numbers[key])[1])
            cnt += 1
    return answer


def main():
    print(solution(	["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

if __name__ == "__main__":
    main()