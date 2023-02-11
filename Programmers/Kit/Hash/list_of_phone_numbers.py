from collections import defaultdict

def solution(phone_book):
    key_value_dict = defaultdict(str)
    phone_book.sort()
    for element in phone_book:
        for i in range(len(element)):
            if element[:i+1] in key_value_dict:
                return False
        key_value_dict[element] = 1
    return True
