def splitWordsBySeparator(words, separator):
        final_words = []

        for word in words:
            split_list = word.split(separator)
            for split in split_list:
                if split:
                    final_words.append(split)
        
        return final_words