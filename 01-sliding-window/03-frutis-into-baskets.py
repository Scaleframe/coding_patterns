"""
Problem Statement #

Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""



def fruits_into_baskets(arr):
    window_start = 0
    window_end = 0 
    max_length = 0
    char_frequency = {}

    # expand the sliding window end through the array
    for window_end in range(len(arr)):
        
        # update the char frequency dictionary with 
                            # the values we traverse 
        right_char = arr[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0   
        char_frequency[right_char] += 1
        
        # when max "baskets" are exceeded, prune the 
                        # start of the sliding window
        while len(char_frequency) > 2:
            left_char = arr[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            
            # shrink the window
            window_start += 1 

        # update the max length        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length




if __name__ == "__main__":

    example_1 = ['A', 'B', 'C', 'A', 'C']
    expected_1 = 3

    example_2 = ['A', 'B', 'C', 'B', 'B', 'C']
    expected_2 = 5

    print(f"output: {fruits_into_baskets(example_1)}, exp: {expected_1}")
    print(f"output: {fruits_into_baskets(example_2)}, exp: {expected_2}")

    assert fruits_into_baskets(example_1) == expected_1
    assert fruits_into_baskets(example_2) == expected_2