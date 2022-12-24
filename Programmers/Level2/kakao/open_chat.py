user_info ={}
logs = []
def enter(id, name):
    global user_info
    global logs
    logs.append([id,"님이 들어왔습니다."])
    user_info[id] = name



def leave(id):
    global logs
    logs.append([id, "님이 나갔습니다."])



def change(id, name):
    global user_info
    user_info[id] = name


def solution(record):
    global user_info
    global logs
    for rec in record:
        rec_split = rec.split()
        if rec_split[0] == "Enter":
            enter(rec_split[1], rec_split[2])
        elif rec_split[0] == "Leave":
            leave(rec_split[1])
        else:
            change(rec_split[1], rec_split[2])
    answer = []
    for log in logs:
        answer.append(user_info.get(log[0])+log[1])
    return answer

def main():
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo"]))


if __name__ == "__main__":
    main()
