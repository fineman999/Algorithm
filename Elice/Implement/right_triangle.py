
def calculate(element):
    element.sort()
    if (element[0]**2) + (element[1]**2) == (element[2]**2):
        return 'rightangle'
    return 'triangle'



def main():
    arr = []
    for _ in range(3):
        element = list(map(int,input().split()))
        if len(element) <=2 and element[0] == 0:
            break
        arr.append(calculate(element))
    for ele in arr:
        print(ele)

if __name__ == "__main__":
    main()