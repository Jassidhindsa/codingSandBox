
import heapq

def topKFrequentElements(nums, k):
    num_count_dict = {}
    num_count_list = []
    topkfreqelem = []

    for num in nums:
        if num not in num_count_dict:
            num_count_dict[num] = 1
        else:
            num_count_dict[num] += 1
    
    for num in num_count_dict.keys():
        num_count_list.append([-num_count_dict[num], num])
    
    heapq.heapify(num_count_list)

    while k > 0 and num_count_list:
        val = heapq.heappop(num_count_list)
        print("val: ", val[1])
        topkfreqelem.append(val[1])
        k -= 1

    return topkfreqelem

if __name__ == "__main__":
    print(topKFrequentElements([1], 1))