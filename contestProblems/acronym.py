

def acronym(words, target):
    if len(words) != len(target):
        return False
    
    index = 0

    for word in words:
        if word[0] != target[index]:
            return False
        index += 1
    
    return True



if __name__ == "__main__":
    print(acronym(["alice","bob","charlie"], "abc"))