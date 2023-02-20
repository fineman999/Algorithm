from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    i = 0
    try:
        while cards1 or cards2 and i < len(goal):
            if cards1 and cards1[0] == goal[i]:
                cards1.popleft()
                i += 1
            elif cards2 and cards2[0] == goal[i]:
                cards2.popleft()
                i += 1
            else:
                return  "No"
    except:
        return "Yes"


    answer = ''

    return "Yes"

def main():
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

if __name__ == "__main__":
    main()