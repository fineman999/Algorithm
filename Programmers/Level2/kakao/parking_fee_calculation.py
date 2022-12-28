import math
def changeTime(record):
    times = record.split(":")
    return int(times[0]) * 60 + int(times[1])

def solution(fees, records):
    answer = []
    cars_time = dict()
    cars = dict()
    for record in records:
        record = record.split()
        if record[2] == "IN":
            start_time = changeTime(record[0])
            cars_time[record[1]] = start_time
        if record[2] == "OUT":
            last_time = changeTime(record[0])
            if record[1] not in cars:
                cars[record[1]] = last_time - cars_time.get(record[1])
            else:
                cars[record[1]] += last_time - cars_time.get(record[1])
            cars_time.pop(record[1])

    for car,car_time in cars_time.items():
        if car not in cars:
            cars[car] = 23*60+59 - car_time
        else:
            cars[car] += 23*60+59 - car_time
    for car, car_time in cars.items():

        if car_time <= fees[0]:
            answer.append([car,fees[1]])
        else:
            answer.append([car,fees[1]+math.ceil((car_time - fees[0]) / fees[2])*fees[3]])

    answer.sort(key=lambda x:x[0])
    result = []
    for ele in answer:
        result.append(ele[1])
    return result


def main():
    print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))


if __name__ == "__main__":
    main()
