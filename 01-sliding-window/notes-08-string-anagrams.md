```python

"""
Notes: 

    Example: 
        input array: abbcabc
        pattern to match: abc

    This has a few components to solve: 


    1: 'Sliding window' 

        a: 'grow window': We moves through array until the window size 
                                        matches the pattern length
        
        b: 'shrink window': Then prune the front value from the window and shrink the window
                            use this to maintain the same window length as the pattern length)

    
    [abb]cabc 
        [abbc]abc
            a[bbc]abc
                a[bbca]bc
                    ab[bca]bc
    

    2: Use a 'frequency table' to track how many values matcc

        pattern = abc

            this means we need to find 1 a, 1 b, 1 c in our given window.
        
            freq_table = {'a': 1, 'b': 1, 'c': 1}
            

        if pattern = aabc 

            then we need to find 2 a's, 1 b, and 1 c in the sliding window. 

            then freq_table = {'a': 2, 'b': 1, 'c': 1}


    3: 'Counting matches'

        - A: we want to use a "matched counter" to keep track of how many of the chars we have
                                            that match the pattern in the frequency table. 


        - B: we '*decrement*' a value in the 'frequency table' when we see a value in the window that matches. 
        
            pattern: abc 
            string: abbcabc
            freq_table = {'a': 1, 'b': 1, 'c': 1}
        
            sliding window: [abb]cabc
            freq_table = {'a': 0, 'b': -1, 'c': 1} (decrement 'a' by 1, 'b' by 2)
            

        - C: we '*increment*' the "match counter" when a value in the frequency table hits 0

            matched = 2 (a is 0, and b is -1. 
                                    (-1 is ok for matched counter, it just means we have one more b than we need). 
            

        - D: re increment "frequency values" when shrinking the window  
            
            original: [abb]cabc
            new:      a[bbc]abc

                old freq_table = {'a': 0, 'b': -1, 'c': 1}      
                old matched = 2: 1 'a' and 2 'b's. 
                                negative 1 is ok for matched, it just means we have one more b than we need). 

            original: [abb]cabc
            new: a[bbc]abc

            - Remove 'a' from the left of window, we are one further away from a match for 'a'
                                            (meaning we *increment* value in freq table for 'a')

                
            interim freq_table = {'a': 1, 'b': -1, 'c': 1}
            interm matched = 1: 2 'b's. (A is no longer a match)    

            - Add 'c' to right of window, we are one closer to a match for 'c'
                                            (meaning we *decrement* the value in freq table for 'c')
                                                            
                
            new freq_table = {'a': 1, 'b': -1, 'c': 0}
            new matched = 2: 2 'b's and 1 'c' 
    

    4: 'Full pattern match and answer':

        - 'if matched counter matches the length of your frequency table' (the number of letters to match), 
                            then you have a 'full pattern match' and can add it to your answer however you need.

            
            original: a[bbc]abc
            new:      ab[bca]bc
                
                - remove b from the left of the window and increment (make further away from a match)
                freq_table = {'a': 1, 'b': 0, 'c': 0}

                - add a to the right of the window, and decrement (make closer to a match)
                freq_table = {'a': 0, 'b': 0, 'c': 0}
                
                matched counter == len(freq_table) --> ***we have a full pattern match***


    Fin: now you can do something with your answer, in this case add the starting index of the sliding window to the result. 
