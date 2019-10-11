import random
import uuid

def get_random_ints(amount, lower_boundary=0, upper_boundary=1000):
    return [random.randint(lower_boundary, upper_boundary) for i in range(amount)]

def get_random_floats(amount, lower_boundary=0, upper_boundary=999.99):
    return [random.uniform(lower_boundary, upper_boundary) for i in range(amount)]

class Employee:
    def __init__(self,employee_id,age):
        self.employee_id = employee_id
        self.age = age
               

def get_random_employees(amount):
    employees = []
    for i in range(amount):
        curr_employee = Employee(uuid.uuid4(),random.randint(20,70))
        employees.append(curr_employee)
    return employees

