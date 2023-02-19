

def solution(book_time):
    times = [0]*24*60 + [0]*10
    for start, end in book_time:
        start_time = int(start.split(":")[0])*60 + int(start.split(":")[1])
        end_time = int(end.split(":")[0]) * 60 + int(end.split(":")[1])
        times[start_time] += 1
        # if end_time + 10 > 24*60:
        #     times[end_time + 10 - 24*60] -= 1
        # else:
        times[end_time + 10] -= 1
        # for i in range(start_time, end_time + 1 + 9):
        #     if i > 24*60:
        #         times[i -24*60] += 1
        #     else:
        #         times[i] += 1
    cnt = 0
    for i in range(len(times)):
        cnt += times[i]
        times[i] = cnt

    return max(times)


def main():
    print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))

if __name__ == "__main__":
    main()