""""search linearly one by one until you find the element
"""

# element_list=[]
"""The time complexity of the algorithm is cN for some fixed constant c that depends on the number of operations we 
perform in each iteration and the time taken to execute a statement. Time complexity is sometimes also called the 
running time of the algorithm. 

The space complexity is some constant c' (independent of N), since we just need a single variable position to iterate 
through the array, and it occupies a constant space in the computer's memory (RAM). 

Big O Notation: Worst-case complexity is often expressed using the Big O notation. In the Big O, we drop fixed 
constants and lower powers of variables to capture the trend of relationship between the size of the input and the 
complexity of the algorithm i.e. if the complexity of the algorithm is cN^3 + dN^2 + eN + f, in the Big O notation it 
is expressed as O(N^3) 

Thus, the time complexity of linear search is O(N) and its space complexity is O(1).
"""


def linear_search(element_list, ele):
    position = 0
    while position < len(element_list):
        if element_list[position] == ele:
            return position
        position += 1
    return -1


print(linear_search([13, 11, 10, 7, 4, 3, 1, 0], 3))
print(linear_search([13, 11, 10, 7, 4, 3, 1, 0], 1))
print(linear_search([4, 2, 1, -1], 4))
print(linear_search([4, 2, 1, -1], 10))
