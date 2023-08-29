


def longestSubstringWithoutRepeatingChars(string):
    longest_string = ""
    left_index = 0
    curr_char_dict = {}

    for index, char in enumerate(string):
        if char in curr_char_dict:
            index_of_existing = curr_char_dict[char]

            for ind in range(left_index, index_of_existing+1):
                curr_char_dict.pop(string[ind])
            
            left_index = index_of_existing + 1
        
        curr_char_dict[char] = index
        if index - left_index + 1 > len(longest_string):
            longest_string = string[left_index:index+1]
    return longest_string



def longestLengthSubstringWithoutRepeatingChars(string):
    longest_string = 0
    left_index = 0
    curr_char_set = set()

    for char in string:
        if char in curr_char_set:
            while char in curr_char_set:
                curr_char_set.remove(string[left_index])
                left_index += 1
        
        curr_char_set.add(char)
        longest_string = max(longest_string, len(curr_char_set))
    return longest_string
 

if __name__ == "__main__":
    print(longestSubstringWithoutRepeatingChars("abcabcbb"))