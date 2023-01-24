import copy
result = set()
def dfs(n, user_id, dictionary, visited):
    global result
    if n == visited.count(True):
        check = []
        for i in range(len(user_id)):
            if visited[i]:
                check.append(user_id[i])
        result.add(tuple(check))
        return

    for i in range(len(user_id)):
        if not visited[i]:
            for key,value in dictionary.items():
                if dictionary[key]>0 and check_banned_valid(user_id[i], key):
                    new_dictionary = copy.deepcopy(dictionary)
                    new_dictionary[key] -= 1
                    new_visited = copy.deepcopy(visited)
                    new_visited[i] = True
                    visited[i] = True
                    dfs(n, user_id, new_dictionary, new_visited)
                    visited[i] = False
    return

def check_banned_valid(user, banned):
    valid = False
    if len(banned) == len(user):
        valid = True
        for i in range(len(banned)):
            if banned[i] == "*":
                continue
            if banned[i] != user[i]:
                valid = False
                break
    return valid
def solution(user_id, banned_id):

    n = len(banned_id)
    dictionary = dict()
    for i in banned_id:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    for i in range(len(user_id)):
        for key,value in dictionary.items():
            if dictionary[key] > 0 and check_banned_valid(user_id[i],key):
                visited = [False] * len(user_id)
                new_dictionary = copy.deepcopy(dictionary)
                new_dictionary[key] -= 1
                visited[i] = True
                dfs(n, user_id, new_dictionary, visited)

    return len(result)


def main():
    print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))


if __name__ == "__main__":
    main()