"""
Permutation in a String (hard) #

Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

    abc
    acb
    bac
    bca
    cab
    cba

If a string has ‘n’ distinct characters, it will have n!n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""
from collections import defaultdict

def permutation_of_string(str, pattern):
    window_start, matched = 0, 0
    char_frequency = defaultdict(int)

    # populate a hashmap with the pattern
    for chr in pattern:
        char_frequency[chr] += 1
    

    # move through the array adding to hashmap unitl all chrs 
                                     # in pattern are present
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        
        # subtract chars that match anything that appears in 
                                         # 'pattern' hashmap
        if right_char in char_frequency:
            char_frequency[right_char] -= 1

            # when char frequency hits zero, increment matched
                                                     # counter 
            if char_frequency[right_char] == 0:
                matched += 1
                
        # the trick: matched counter has same count as pattern 
        # hasmap has indexes. 
        
        # Example:
            # {b:2} needs to find 2 b's in array to increment match,
            # then condition is met
                                                    
        if matched == len(char_frequency):
            return True

        # Handle disjoint permutation chars. Example: if pattern is 
        # abd, and bc are found followed by x, permuataion is broken.
        if window_end >= len(pattern) -1:
            
            # So remove front char, reset match and continue through the 
                                                                 # array.
            left_char = str[window_start]
            window_start += 1
            
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:

                    matched -= 1
                char_frequency[left_char] += 1
    
    return False


if __name__ == "__main__":
    
    example_1 = "oidbcaf"
    k_1 = "abc"
    expected_1 = True


    example_2 = "odicf"
    k_2 = "dc"
    expected_2 = False


    example_3 = "bcdxabcdy"
    k_3 = "bcdyabcdx"
    expected_3 = True


    example_4 = "aaacb"
    k_4 = "abc"
    expected_4 = True


    print(f"output: {permutation_of_string(example_1, k_1)}, exp: {expected_1}")
    print(f"output: {permutation_of_string(example_2, k_2)}, exp: {expected_2}")
    print(f"output: {permutation_of_string(example_3, k_3)}, exp: {expected_3}")
    print(f"output: {permutation_of_string(example_4, k_4)}, exp: {expected_4}")

    assert permutation_of_string(example_1, k_1) == expected_1
    assert permutation_of_string(example_2, k_2) == expected_2
    assert permutation_of_string(example_3, k_3) == expected_3
    assert permutation_of_string(example_4, k_4) == expected_4

    print("-"*20)
    print("All Tests Passed!")