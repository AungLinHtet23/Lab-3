import employee_info

# Test case for get_employees_by_age_range
def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(25, 35)
    expected = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    ]
    # Sort both lists by name to avoid ordering issues
    result_sorted = sorted(result, key=lambda x: x["name"])
    expected_sorted = sorted(expected, key=lambda x: x["name"])
    
    assert result_sorted == expected_sorted


# Test case for calculate_average_salary
def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    expected_average = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6  # Expected average
    assert result == expected_average

# Test case for get_employees_by_dept
def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Sales")
    expected = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000},
    ]
    assert result == expected
