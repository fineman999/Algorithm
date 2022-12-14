def solution(cacheSize, cities):
    cache = []
    answer = 0
    for city in cities:
        if city.lower() in cache:
            for i in range(len(cache)):
                if city.lower() == cache[i]:
                    pop = cache.pop(i)
                    cache.append(pop)
                    break
            answer += 1

        else:
            cache.append(city.lower())
            answer += 5
            if len(cache) > cacheSize:
                cache.pop(0)

    return answer

def main():
    print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))


if __name__ == "__main__":
    main()
