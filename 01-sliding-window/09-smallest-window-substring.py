"""
Smallest Window containing Substring (hard) #

Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.


"""

def find_substring(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1
    

    # extend until we have all letter in the pattern
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0: # we're already in the block, so you can add any value >= 0 for a match. 

                matched += 1


        # shrink window if we can, finish as soon as we remove a matched char
        while matched == len(pattern):
            print("**pattern match**")
            print("----shrinking window-----")
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                print(f"min length: {min_length}")
                substr_start = window_start
        
            left_char = str1[window_start]
            window_start += 1
            print(f"shrunk window: {str1[window_start:window_end + 1]}")
            if left_char in char_frequency:
                # only decrement if there are non duplicate chars in window
                if char_frequency[left_char] == 0:
                    matched -= 1
                    print(f"matched -= 1 => {matched}")
                char_frequency[left_char] += 1
                print(f"shrunk char frequency: {char_frequency}")

    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]


if __name__ == "__main__":
    
    example_1 = "aabdec"
    k_1 = "abc"
    expected_1 = "abdec"


    example_2 = "abdbca"
    k_2 = "abc"
    expected_2 = "bca"


    example_3 = "adcad"
    k_3 = "abc"
    expected_3 = ""


    print(f"output: {find_substring(example_1, k_1)}, exp: {expected_1}")
    print(f"output: {find_substring(example_2, k_2)}, exp: {expected_2}")
    print(f"output: {find_substring(example_3, k_3)}, exp: {expected_3}")


    assert find_substring(example_1, k_1) == expected_1
    assert find_substring(example_2, k_2) == expected_2
    assert find_substring(example_3, k_3) == expected_3

    print("-"*20)
    print("All Tests Passed!")