

def finalString(self, s: str) -> str:
    index = 0
    while index < len(s):
        char = s[index]
        if char == "i":
            prev_string = s[:index][::-1]
            s = prev_string + s[index+1:]
        else:
            index += 1
    
    return s