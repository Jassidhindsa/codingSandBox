


def validAnagram(string_s, string_t):
    char_count_dict = {}

    for char in string_s:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    
    for char in string_t:
        if char not in char_count_dict:
            return False
        elif char_count_dict[char] == 0:
            return False
        else:
            char_count_dict[char] -= 1
    
    if sum(char_count_dict.values()) != 0:
        return False
    
    return True


def validAnagramBetter(string_s, string_t):
    if len(string_s) != len(string_t):
        return False
    
    char_dict_string_s = {}
    char_dict_string_t = {}

    for i in range(len(string_s)):
        if string_s[i] not in char_dict_string_s:
            char_dict_string_s[string_s[i]] = 1
        else:
            char_dict_string_s[string_s[i]] += 1
        
        if string_t[i] not in char_dict_string_t:
            char_dict_string_t[string_t[i]] = 1
        else:
            char_dict_string_t[string_t[i]] += 1
    
    return char_dict_string_s == char_dict_string_t
 


if __name__ == "__main__":
    print(validAnagramBetter("anagrama", "nagaram"))