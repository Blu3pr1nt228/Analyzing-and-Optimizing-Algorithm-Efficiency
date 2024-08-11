# Test Cases


import bubble_sort



def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90], "Test Case 1 Failed"
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8], "Test Case 2 Failed"
    assert bubble_sort([3, 3, 3]) == [3, 3, 3], "Test Case 3 Failed"
    assert bubble_sort([1]) == [1], "Test Case 4 Failed"
    assert bubble_sort([]) == [], "Test Case 5 Failed"

    print("All Bubble Sort test cases passed!")

# Run the test cases



if __name__ == "__main__":
    
    test_bubble_sort()
    print("All tests passed!")
