import itertools


def solution(user_id, banned_id):
    arr = []


    for banned in banned_id:
        for user in user_id:
            if len(banned) == len(user):
                valid = True
                for i in range(len(banned)):
                    if banned[i] == "*":
                        continue
                    if banned[i] != user[i]:
                        valid = False
                        break
                if valid:
                    arr.append(user)
    s = set(arr)
    combinations = itertools.combinations(s, len(banned_id))

    return s



def main():
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))


if __name__ == "__main__":
    main()