"""
Problem Statement #

Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""
from collections import defaultdict


def longest_substring(str, k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    frequency_map = defaultdict(int)

    # expand window forward, adding values frequency table
    for window_end in range(len(str)):
        right_char = str[window_end]
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])
        
    
        # check if window has > k "extra slots" open. 
                            # if not, shrink window.
                            # (notes below) 
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char =  str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1 

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


"""
Notes:

    Take the example abbcbbc, k=2

    We want to move through the string adding to frequency_count

        a, b, b, c, b, b, c
        a:1, b:1, b:2, c:1, b:3, b:4, c: 2

    To get the max length, we want to return the legnth of this window

    However, there is condition we want to shrink the window, 

        whenever there is more room in the window than there is 
        k places to replace characters. Take the string above.

    [a, b, b, c, b, b,] c <--- you can safely grow your window until here.
        why? 
            window size is 6 
            max_repeating currently is 4
            window size - max repeating gives you "spaces left"
            "spaces left" is what you can replace
            if you make sure "spaces left" = k, you are in business. 
"""



if __name__ == "__main__":

    example_1 = "aabccbb"
    k_1 = 2
    expected_1 = 5


    example_2 = "abbcb"
    k_2 = 1
    expected_2 = 4


    example_3 = "abccde"
    k_3 = 1
    expected_3 = 3

    print(f"output: {longest_substring(example_1, 2)}, exp: {expected_1}")
    print(f"output: {longest_substring(example_2, 1)}, exp: {expected_2}")
    print(f"output: {longest_substring(example_3, 1)}, exp: {expected_3}")

    assert longest_substring(example_1, 2) == expected_1
    assert longest_substring(example_2, 1) == expected_2
    assert longest_substring(example_3, 1) == expected_3

    print("-"*20)
    print("All Tests Passed!")