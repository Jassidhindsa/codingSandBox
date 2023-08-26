

def maxLengthOfChainPair(pairs):
    pairs.sort(key = lambda x : (x[1], x[0]))

    max_length = 1
    last_good_pair = None

    for pair in pairs:
        if not last_good_pair:
            last_good_pair = pair
        else:
            last_pair_end = last_good_pair[1]
            if last_pair_end < pair[0]:
                max_length += 1
                last_good_pair = pair

    return max_length                






if __name__ == "__main__":
    print(maxLengthOfChainPair([[1,2],[2,3],[3,4]]))