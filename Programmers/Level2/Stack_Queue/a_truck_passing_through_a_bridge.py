from collections import deque

def solution(bridge_length, weight, truck_weights):
    all_truck = len(truck_weights)
    completed_pass_truck = 0
    cross_pass_truck = deque()
    timer_pass_truck = []
    time_count = 0
    while completed_pass_truck != all_truck:
        time_count += 1
        try:
            for i in range(len(timer_pass_truck)):
                timer_pass_truck[i] += 1
            if timer_pass_truck[0] == bridge_length:
                cross_pass_truck.popleft()
                timer_pass_truck.pop(0)
                completed_pass_truck += 1
        except:
            pass

        try:
            if sum(cross_pass_truck) + truck_weights[0] <= weight:
                truck_weights_pop = truck_weights.pop(0)
                cross_pass_truck.append(truck_weights_pop)
                timer_pass_truck.append(0)
        except:
            continue

    return time_count



def main():
    print(solution(2, 10, [7,4,5,6]))


if __name__ == "__main__":
    main()
