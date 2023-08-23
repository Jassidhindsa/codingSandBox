



def productOfArrayExceptItself(nums):
    total_prod = 1
    total_negs = 0
    total_zeroes = 0
    output = []

    for num in nums:
        if num != 0:
            total_prod *= abs(num)
            if num < 0:
                total_negs += 1
        else:
            total_zeroes += 1
    print(total_prod, total_negs, total_zeroes)
    for num in nums:
        if num == 0:
            if total_zeroes > 1:
                output.append(0)
            else:
                val = (total_prod) if total_negs % 2 == 0 else -1*(total_prod)
                output.append(val)
        elif num < 0:
            if total_zeroes > 0:
                output.append(0)
            elif total_negs > 1:
                val = (total_prod // (abs(num))) if (total_negs -  1) % 2 == 0 else -1*(total_prod // (abs(num)))
                output.append(val)
            else:
                output.append((total_prod // abs(num)))
        else:
            if total_zeroes > 0:
                output.append(0)
            elif total_negs > 0:
                val = (total_prod // (abs(num))) if (total_negs) % 2 == 0 else -1*(total_prod // (abs(num)))
                output.append(val)
            else:
                output.append(total_prod // (abs(num)))

    return output

if __name__ == "__main__":
    print(productOfArrayExceptItself([5,9,2,-9,-9,-7,-8,7,-9,10]))