
def solution(nums):
    return min(len(nums)//2, len(set(nums)))

def main():
    print(solution(	[3, 1, 2, 3]))

if __name__ == "__main__":
    main()
