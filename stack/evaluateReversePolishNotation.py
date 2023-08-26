

def evaluateReversePolishNotation(tokens):
    num_stack = []
    operations = ["+", "-", "*", "/"]

    for token in tokens:
        if token not in operations:
            num_stack.append(int(token))
        else:
            num_2, num_1 = num_stack.pop(), num_stack.pop()
            if token == "+":
                new_num = num_1 + num_2
                num_stack.append(new_num)
            elif token == "-":
                new_num = num_1 - num_2
                num_stack.append(new_num)
            elif token == "*":
                new_num = num_1 * num_2
                num_stack.append(new_num)
            else:
                new_num = int(num_1 / num_2)
                num_stack.append(new_num)
    return num_stack[0]

if __name__ == "__main__":
    print(evaluateReversePolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))