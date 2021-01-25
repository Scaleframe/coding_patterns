"""
String Anagrams #

Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

    abc
    acb
    bac
    bca
    cab
    cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""


def find_string_anagrams(str1, pattern):
    window_start, matched = 0, 0 
    char_frequency = {}

    # build frequency table for pattern matching
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    result_indicies = [] # answer list

    # extend window forward
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        
        # now we decrement values we find from the frequency table
        if right_char in char_frequency:
            char_frequency[right_char] -= 1

            # until we get to a zero value, then we increment matched counter by 1. 
            if char_frequency[right_char] == 0:
                # logging.debug("matched + 1")
                matched += 1
        
        
        # the goal condition: when matched counter is equeal to length of chars in 
                                         # freq table, we have a full pattern match
        
        if matched == len(char_frequency): 
            result_indicies.append(window_start)
        
        # shrink sliding window when the window size is > the len of the pattern 
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            
            # the left char should not count towards matched anymore
            if left_char in char_frequency: 
                if char_frequency[left_char] == 0:
                    matched -= 1
                    # print("matched - 1: ", matched)
                char_frequency[left_char] += 1 # put left char back

    return result_indicies    


if __name__ == "__main__":
    
    example_1 = "ppqp"
    k_1 = "pq"
    expected_1 = [1,2]


    example_2 = "abbcabc"
    k_2 = "abc"
    expected_2 = [2, 3, 4]


    print(f"output: {find_string_anagrams(example_1, k_1)}, exp: {expected_1}")
    print(f"output: {find_string_anagrams(example_2, k_2)}, exp: {expected_2}")


    assert find_string_anagrams(example_1, k_1) == expected_1
    assert find_string_anagrams(example_2, k_2) == expected_2


    print("-"*20)
    print("All Tests Passed!")
