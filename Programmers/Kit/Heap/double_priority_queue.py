import heapq
def solution(operations):
    heap = []
    for operate in operations:
        [types, number] = operate.split()
        number = int(number)
        if types == 'I':
            heapq.heappush(heap, number)
        elif types == 'D' and heap:
            if number > 0:
                heap.pop()
            else:
                heapq.heappop(heap)
    if heap:
        heap.sort()
        return [heap[-1],heap[0]]

    return [0,0]



def main():
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))


if __name__ == "__main__":
    main()
