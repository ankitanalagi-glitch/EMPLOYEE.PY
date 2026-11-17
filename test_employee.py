from employee import employee_details

def test_employee_details():
    result = employee_details(
        "Rahul",
        101,
        "Computer Science",
        50000
    )

    expected = (
        "Employee Name: Rahul\n"
        "Employee ID: 101\n"
        "Department: Computer Science\n"
        "Salary: 50000"
    )

    assert result == expected
    
