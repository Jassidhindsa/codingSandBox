

def minimumString(a, b, c):

    def checkPossibility(string1, string2):
        if string2 in string1:
            return string1
        else:

            for index in range(len(string1)):
                if string2.startswith(string1[index:]):
                    return string1[:index] + string2
            
            return string1+string2
    

    possibilities = [
        checkPossibility(checkPossibility(a, b), c),
        checkPossibility(checkPossibility(b, a), c),
        checkPossibility(checkPossibility(b, c), a),
        checkPossibility(checkPossibility(c, b), a),
        checkPossibility(checkPossibility(a, c), b),
        checkPossibility(checkPossibility(c, a), b),
    ]
    
    min_length, min_string = float('inf'), ''
    for possibility in possibilities:
        if len(possibility) < min_length:
            min_length = len(possibility)
            min_string = possibility
        elif len(possibility) == len(min_string):
            min_string = min(min_string, possibility)
    
    return min_string
