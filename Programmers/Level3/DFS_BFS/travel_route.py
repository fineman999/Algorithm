from collections import defaultdict
import copy


check = []


def set_dictionary(tickets, dictionary):
    for start, end in tickets:
        dictionary[start].append(end)


def dfs(answer, dictionary):

    if not dictionary:
        global check
        check.append(answer)
        return

    if answer[-1] in dictionary:
        get_tickets = dictionary[answer[-1]]

        for ticket in get_tickets:
            new_dictionary = copy.deepcopy(dictionary)
            new_dictionary[answer[-1]].remove(ticket)
            if not new_dictionary[answer[-1]]:
                del new_dictionary[answer[-1]]
            new_answer = copy.deepcopy(answer)
            new_answer.append(ticket)
            dfs(new_answer, new_dictionary)


def solution(tickets):
    answer = []
    dictionary = defaultdict(list)
    set_dictionary(tickets, dictionary)
    answer.append("ICN")

    dfs(answer, dictionary)
    global check
    check.sort()
    return check[0]


def main():
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))


if __name__ == "__main__":
    main()
