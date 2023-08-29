


def longestRepeatingCharReplacement(string, k):
    count_dict = {}

    left_index = 0
    max_freq = 0

    for right_index in range(len(string)):
        if string[right_index] not in count_dict:
            count_dict[string[right_index]] = 1
        else:
            count_dict[string[right_index]] += 1
        
        max_freq = max(max_freq, count_dict[string[right_index]])

        if (right_index - left_index + 1) - max_freq > k:
            count_dict[string[left_index]] -= 1
            left_index += 1

    return (right_index - left_index + 1) 


if __name__ == "__main__":
    print(longestRepeatingCharReplacement("ABBB", 2))