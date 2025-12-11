from emp import emp_details

def test_employee_details():
    expected_output = (
        "Employee Name: arya\n"
        "Employee ID: 111\n"
        "Employee Department: IIT\n"
        "Employee Salary: 55000\n"
    )

    result = emp_details("arya", "111", "IIT", "55000")
    assert result == expected_output