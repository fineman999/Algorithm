


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    cnt = 0
    while bridge or truck_weights:
        truck = truck_weights.pop(0)
        bridge.append([truck, 0])
        # 다리 길이 확인
        valid = True
        if sum(bridge) > weight:
            valid = False
            truck_weights.insert(0, bridge.pop())

        if valid:
            cnt += 1



    return answer

def main():
    print(solution(2, 10, [7,4,5,6]))


if __name__ == "__main__":
    main()
