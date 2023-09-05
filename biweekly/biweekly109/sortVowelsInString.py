

# save indices of vowels in set
# if found vowel put it in heap
# then start iterating for length of string
# if consonant then add it as it is
# if vowel the pop from the heap
import heapq

def sortVowels(s):
    vowels_indices = set()
    vowels_heap = []
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    vowels_set = set(vowels)

    for index, char in enumerate(s):
        if char in vowels_set:
            vowels_indices.add(index)
            heapq.heappush(vowels_heap, char)
    
    final_string = ""

    for index in range(len(s)):
        if index not in vowels_indices:
            final_string += s[index]
        else:
            final_string += heapq.heappop(vowels_heap)
    
    return final_string