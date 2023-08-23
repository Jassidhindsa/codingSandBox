


def groupAnagrams(words):
    words_dict = {}

    for word in words:
        ordered_word = "".join(sorted(word))
        if ordered_word in words_dict:
            words_dict[ordered_word].append(word)
        else:
            words_dict[ordered_word] = [word]
    
    output = list(words_dict.values())
    return output

if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))