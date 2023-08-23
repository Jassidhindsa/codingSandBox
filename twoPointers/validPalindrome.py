
def validPalindrome(string):
    final_string = ""

    for char in string:
        if char.isalpha():
            final_string += char.lower()
        elif char.isdigit():
            final_string += char

    left_pointer, right_pointer = 0, len(final_string) - 1
    
    while left_pointer < right_pointer:
        if final_string[left_pointer] != final_string[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
    
    return True

if __name__ == "__main__":
    print(validPalindrome("A man, a plan, a canal: Panama"))