


def carFleet(target, position, speed):
    fleet_stack = []
    fleet_list = []
    car_fleet_count = 0

    def popAppend(fleet_stack, position, speed):
        if fleet_stack == []:
            fleet_stack.append([position, speed])
            return
        elif position == fleet_stack[-1][0]:
            min_speed = min(fleet_stack[-1][1], speed)
            fleet_stack.append([position, min_speed])
            return
        else:
            popped_car = fleet_stack[-1]
            fleet_stack = fleet_stack[:-1]
            popAppend(fleet_stack, position, speed)
            fleet_stack.append(popped_car)
            return

    for index in range(len(position)):
        popAppend(fleet_stack, position[index], speed[index])
    
    print(fleet_stack)


if __name__ == "__main__":
    print(carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))