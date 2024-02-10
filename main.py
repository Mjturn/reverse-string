def reverse_string(string):
    string_list = list(string)
    
    left_pointer = 0
    right_pointer = len(string) - 1

    while left_pointer < right_pointer:
        temp = string_list[left_pointer]
        string_list[left_pointer] = string_list[right_pointer]
        string_list[right_pointer] = temp
        left_pointer += 1
        right_pointer -= 1

    return "".join(string_list)

print(reverse_string("Cat"))
