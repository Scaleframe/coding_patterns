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
    pass












example_1 = ['A', 'B', 'C', 'A', 'C']
expected_1 = 3


example_2 = ['A', 'B', 'C', 'B', 'B', 'C']
expected_2 = 5 


if __name__ == "__main__":
    
    print(f"output: {fruits_into_baskets(example_1)}, exp: {expected_1}")
    print(f"output: {fruits_into_baskets(example_2)}, exp: {expected_2}")

    assert fruits_into_baskets(example_1) == expected_1
    assert fruits_into_baskets(example_2) == expected_2