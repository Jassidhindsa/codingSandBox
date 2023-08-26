


def dailyTemperatures(temperatures):
    temp_stack = []
    warm_days_list = [0 for i in range(len(temperatures))]

    for index, temperature in enumerate(temperatures):
        if temp_stack == []:
            temp_stack.append([temperature, [index]])
        else:
            while temp_stack != [] and temp_stack[-1][0] < temperature:
                print(temperature, temp_stack, warm_days_list)
                prev_index_list = temp_stack[-1][1]
                for prev_index in prev_index_list:
                    warm_days_list[prev_index] = index - prev_index
                    print(index, prev_index)
                temp_stack = temp_stack[:-1]
            if temp_stack != [] and temp_stack[-1][0] == temperature:
                temp_stack[-1][1].append(index)
            else:
                temp_stack.append([temperature, [index]])
    
    return warm_days_list



if __name__ == "__main__":
    print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))