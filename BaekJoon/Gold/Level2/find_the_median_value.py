import sys
import heapq

def solution(M, sequence):
    heap = []
    answer = []

    for i in range(M):
        # heapq.heappush(heap,sequence[i])
        heap.append(sequence[i])
        if i % 2 == 0:
            heap.sort()
            answer.append(heap[len(heap)//2])
    print(len(answer))
    for i in range(len(answer)//10+1):
        print(" ".join(list(map(str,answer[10*(i):10*(i+1)]))))



def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        M = int(sys.stdin.readline().rstrip())
        sequence = []

        for i in range(M//10+1):
            sequence += list(map(int, sys.stdin.readline().rstrip().split()))
        solution(M, sequence)

if __name__ == '__main__':
    main()