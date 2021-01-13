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


def longest_substring(str, k):
    pass





if __name__ == "__main__":

    example_1 = "aabccbb"
    k_1 = 2
    expected_1 = 5


    # example_2 = "abbcb"
    # k_2 = 1
    # expected_2 = 4


    # example_3 = "abccde"
    # k_3 = 1
    # expected_3 = 3

    print(f"output: {longest_substring(example_1, 2)}, exp: {expected_1}")
    # print(f"output: {longest_substring(example_2, 1)}, exp: {expected_2}")
    # print(f"output: {longest_substring(example_3, 1)}, exp: {expected_3}")

    assert longest_substring(example_1, 2) == expected_1
    # assert longest_substring(example_2, 1) == expected_2
    # assert longest_substring(example_3, 1) == expected_3

    print("-"*20)
    print("All Tests Passed!")