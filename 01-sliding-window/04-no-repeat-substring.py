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



def no_repeat_substring(str):
    pass




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