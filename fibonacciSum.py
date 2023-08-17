# Return sum of n fibonacci sequence


def fibonacciSum(n):    
    fibonacci_list = []
    result = 0

    for i in range(n):
        if i <= 1:
            fibonacci_list.append(1)
            result += 1
        else:
            next_val = fibonacci_list[i-1] +  fibonacci_list[i-2]
            fibonacci_list.append(next_val)
            result += next_val

    return result
