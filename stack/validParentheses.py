

def validParentheses(s):
    stack = []
    closing = [')', ']', '}']

    for char in s:
        if char in closing:
            if not stack or (char == ')' and stack[-1] != '(') or (char == ']' and stack[-1] != '[')  or (char == '}' and stack[-1] != '{'):
                return False
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return False
    return True


if __name__ == "__main__":
    print(validParentheses("()[]"))