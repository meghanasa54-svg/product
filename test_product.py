from journal6 import employee_info

def test_employee_info():
    result = employee_info("Rahul", 101, "HR", 25000)

    expected = (
        "Employee Name: Rahul\n"
        "Employee ID: 101\n"
        "Department: HR\n"
        "Salary: 25000"
    )

    assert result == expected
