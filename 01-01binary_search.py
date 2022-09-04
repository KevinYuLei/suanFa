def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = round((low+high)/2)
        guess = list[mid]
        print("guess:", guess)
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9, 11, 13]

# pos "positon"
print("answer to pos:", binary_search(my_list, 1))  # => 1
print("answer to pos:", binary_search(my_list, -1))   # => None
print("answer to pos:", binary_search(my_list, 14))   # => None
