

def solution(priorities, location):
    valid = [False]*len(priorities)
    valid[location] = True
    cnt = 0
    while priorities:
        pop = priorities.pop(0)
        valid_pop = valid.pop(0)
        check = True
        for priority in priorities:
            if pop < priority:
                priorities.append(pop)
                valid.append(valid_pop)
                check = False
                break
        if check:
           cnt += 1
           if valid_pop:
               return cnt

    return 0


def main():
    print(solution([1, 1, 9, 1, 1, 1], 0))


if __name__ == "__main__":
    main()
