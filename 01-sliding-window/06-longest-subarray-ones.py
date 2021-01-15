"""
Problem Statement #

Given an array containing 0s and 1s, if you are allowed to replace no more than
‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray
 of 1s having length 6.

Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray
 of 1s having length 9.
"""

def length_longest_subarray(arr, k):
    pass




if __name__ == "__main__":

    example_1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k_1 = 2
    expected_1 = 6


    example_2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k_2 = 1
    expected_2 = 4


    print(f"output: {length_longest_subarray(example_1, 2)}, exp: {expected_1}")
    print(f"output: {length_longest_subarray(example_2, 1)}, exp: {expected_2}")


    assert length_longest_subarray(example_1, 2) == expected_1
    assert length_longest_subarray(example_2, 1) == expected_2


    print("-"*20)
    print("All Tests Passed!")