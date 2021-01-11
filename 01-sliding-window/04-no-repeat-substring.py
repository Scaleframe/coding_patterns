"""
Problem Statement #

Given a string, find the length of the longest substring, which has no repeating characters.

Example 1:

    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating characters is "abc".

Example 2:

    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring without any repeating characters is "ab".

Example 3:

    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""
from collections import defaultdict


def no_repeat_substring(str):
    # stuff we need to work through the string
    window_start = 0
    window_end = 0
    max_length = 0
    char_frequency = defaultdict(int)

    # move forward through string
    for window_end in range(len(str)):
        
        # add the current pointers char to frequency table
        right_char = str[window_end]        
        char_frequency[right_char] += 1
        
        # this checks for repeated char 
        while char_frequency[right_char] > 1:
            
            # since we have a repeated char, prune values 
                                    # from start of window 
            left_char = str[window_start] 
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]

            # then shrink the window
            window_start += 1

        # update the current non repeating char window length
        current_length = window_end - window_start + 1
        
        # update the max non repeating char window length. 
        max_length = max(max_length, current_length)
    
    return max_length

            

if __name__ == "__main__":

    example_1 ="aabccbb"
    expected_1 = 3

    example_2 = "abbbb"
    expected_2 = 2

    example_3 = "abccde"
    expected_3 = 3

    print(f"output: {no_repeat_substring(example_1)}, exp: {expected_1}")
    print(f"output: {no_repeat_substring(example_2)}, exp: {expected_2}")
    print(f"output: {no_repeat_substring(example_3)}, exp: {expected_3}")

    assert no_repeat_substring(example_1) == expected_1
    assert no_repeat_substring(example_2) == expected_2
    assert no_repeat_substring(example_3) == expected_3

    print("-"*20)
    print("All Tests Passed!")