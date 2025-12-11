def emp_details(name, emp_id, dept, salary):
    result = (
        f"Employee name: {name}\n"
        f"Employee id: {emp_id}\n"
        f"Department: {dept}\n"
        f"Salary: {salary}"
    )
    return result

if _name_ == "_main_":
    name = "sumeet"
    emp_id = 153
    dept = "BCA"
    salary = 20000000
    
    print(emp_details(name, emp_id, dept, salary))