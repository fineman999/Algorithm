
chat_room = []
log = []

def enter(id, name):
    global chat_room
    log.append(f"{name}님이 들어왔습니다.")
    chat_room.append([id, name])


def leave(id):
    global chat_room
    global log
    user_name = ""
    for user in chat_room:
        if user[0] == id:
            user_name = user[1]
            chat_room.remove(user)
    log.append(f"{user_name}님이 나갔습니다.")


def change(id, name):
    global chat_room
    global log
    change_name = ""
    for i in range(len(chat_room)):
        if chat_room[i][0] == id:
            change_name = chat_room[i][1]
            chat_room[i][1] = name

    for i in range(len(log)):
        if change_name in log[i]:
            log[i] = f"{name}님이 " + log[i].split(" ")[1]

def solution(record):
    global log
    for rec in record:

        message = rec.split()
        if message[0] == "Enter":
            enter(message[1], message[2])
        elif message[0] == "Leave":
            leave(message[1])
        else:
            change(message[1], message[2])


    return log


def main():
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo"]))


if __name__ == "__main__":
    main()
