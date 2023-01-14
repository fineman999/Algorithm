
melody = { "C", "C#", "D", "D#", "E", "F", "F#", "G","G#", "A", "A#", "B","E#" }
def change(content):
    new_content = []
    n = len(content)
    check_melody = ""
    for i in range(n - 1, -1, -1):
        if check_melody in melody:
            new_content.append(check_melody)
            check_melody = content[i]
        else:
            check_melody = content[i] + check_melody
    if check_melody in melody:
        new_content.append(check_melody)
    return new_content[::-1]


def solution(m, musicinfos):
    musics = dict()
    for music in musicinfos:
        start_time, end_time, name, content = music.split(",")
        start_time = int(start_time.split(":")[0])*60 + int(start_time.split(":")[1])
        end_time = int(end_time.split(":")[0]) * 60 + int(end_time.split(":")[1])
        long_time = end_time - start_time

        new_content = change(content)
        n = len(new_content)
        if long_time >= n:
            new_content = new_content * long_time
        musics[name] = new_content[:long_time+1]
    m = change(m)
    answer = []
    for key, value in musics.items():
        for i in range(len(value)):
            if value[i] == m[0]:
                valid = True
                for j in range(1, len(m)):
                    if i + j >= len(value)-1:
                        # if m[j] != value[len(value)%(j + i)]:
                        valid = False
                        break
                    elif m[j] != value[j+i]:
                        valid = False
                        break
                if valid:
                    answer.append([key, len(value)])

    if answer:
        answer.sort(key=lambda x:x[1],reverse=True)
        return answer[0][0]
    return "(None)"

def main():
    print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))


if __name__ == "__main__":
    main()