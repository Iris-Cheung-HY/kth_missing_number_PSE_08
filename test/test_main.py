from main.main import find_kth_missing_positive_number


def test_normal_case_with_input_and_missing():
    nums = [2,3,4,7,11]
    kth_missing = 5
    
    # act
    result = find_kth_missing_positive_number(nums, kth_missing)
    # assert
    assert result == 9

def test_normal_case_with_first_4th_input():
    nums = [1,2,3,4]
    kth_missing = 2
        
    # act
    result = find_kth_missing_positive_number(nums, kth_missing)
    # assert
    assert result == 6

def test_normal_case_with_no_input():
    nums = []
    kth_missing = 5
    
    # act
    result = find_kth_missing_positive_number(nums, kth_missing)
    # assert
    assert result == 5

def test_normal_case_with_no_input():
    nums = [1,1000]
    kth_missing = 980
    
    # act
    result = find_kth_missing_positive_number(nums, kth_missing)
    # assert
    assert result == 981


# test from learn

def test_find_kth_missing_positive_number_when_number_is_before_list():
    # Arrange
    numbers = [2, 3, 4, 7, 11]
    kth_missing = 1

    # Act
    result = find_kth_missing_positive_number(numbers, kth_missing)

    # Assert
    assert result == 1

def test_find_kth_missing_positive_number_finds_number_near_end_of_list():
    # Arrange
    numbers = [2, 3, 4, 7, 11]
    kth_missing = 5

    # Act
    result = find_kth_missing_positive_number(numbers, kth_missing)
    
    # Assert
    assert result == 9

def test_find_kth_missing_positive_number_when_number_is_after_list():
    # Arrange
    numbers = [1, 2, 3, 4]
    kth_missing = 2

    # Act
    result = find_kth_missing_positive_number(numbers, kth_missing)
    
    # Assert
    assert result == 6 

def test_find_kth_missing_positive_number_2nd_number_before_list_starts():
    # Arrange
    numbers = [3, 4, 5, 7, 11]
    kth_missing = 2

    # Act
    result = find_kth_missing_positive_number(numbers, kth_missing)
    
    assert result == 2