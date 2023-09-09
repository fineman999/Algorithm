import heapq

def solution(ability, number):
    
    heapq.heapify(ability)
    
    for _ in range(number):
        per1 = heapq.heappop(ability)
        per2 = heapq.heappop(ability)
        heapq.heappush(ability, per1 + per2)
        heapq.heappush(ability, per1 + per2)
    
    return sum(ability)


def main():
    ability = [10, 3, 7, 2]
    number = 2
    print(solution(ability=ability, number=number))
    


if __name__ == "__main__":
    main()