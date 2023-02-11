from collections import defaultdict

def solution(participant, completion):
    key_values = defaultdict(int)
    for person in participant:
        key_values[person] += 1
    for person in completion:
        key_values[person] -= 1
        if key_values[person] == 0:
            del key_values[person]

    return list(key_values.keys())[0]

def main():
    print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

if __name__ == "__main__":
    main()
