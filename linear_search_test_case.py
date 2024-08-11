# Test Cases


import linear_search



def test_linear_search():
    array = [10, 23, 45, 70, 11, 15]
    
    assert linear_search(array, 70) == 3, "Test Case 1 Failed"
    assert linear_search(array, 11) == 4, "Test Case 2 Failed"
    assert linear_search(array, 99) == -1, "Test Case 3 Failed"
    assert linear_search([], 1) == -1, "Test Case 4 Failed"
    assert linear_search([1], 1) == 0, "Test Case 5 Failed"
    assert linear_search([2], 1) == -1, "Test Case 6 Failed"

    print("All Linear Search test cases passed!")

# Run the test cases
test_linear_search()
# test_algorithms.py

import linear_search




if __name__ == "__main__":
    test_linear_search()
    test_bubble_sort()
    print("All tests passed!")
