def solution(people, limit):
    people.sort()
    print(people)
    cnt = 0
    sum_person = 0
    member = 0
    for person in people:
        sum_person += person
        member += 1
        if sum_person > limit or member > 2:
            cnt += 1
            sum_person = person
            member = 1

    cnt += 1
    return cnt



def main():
    people = [70, 50, 80, 50]
    limit = 100
    print(solution(people, limit))


if __name__ == "__main__":
    main()
