# 1. Write a OOP in python to input empid, name, basic salary, no. of experience in yrs. Calculate hra(35% of basic), da (58% of basic) and pf (9.5% of basic).
# Also calculate bonus based on experience in years.
# If experience in years is >= 30, bonus must be 59% of basic, If experience in years is >=23, bonus must be 51% of basic, If experience in years is >=15, bonus must be 45% of basic, If experience in years is >=7, bonus must be 33% of basic, If experience in years is <7, bonus must be 16% of basic Calculate netsalary as basic+da+hra-pf+bonus.
# Create a class, constructor to create instance variables, getter-setter for each variable, calculative functions for operative variables. A class methods/function should not contain
# display specific and input specific code. Such code should be added in driver part of
# python program.


class Employee:
    def __init__(self, empid, name, basic_salary, experience_years):
        self.empid = empid
        self.name = name
        self.basic_salary = basic_salary
        self.experience_years = experience_years

# Getter method
    def get_empid(self):
        return self.empid

    def get_name(self):
        return self.name

    def get_basic_salary(self):
        return self.basic_salary

    def get_experience_years(self):
        return self.experience_years

# Setter method
    def set_empid(self, empid):
        self.empid = empid

    def set_name(self, name):
        self.name = name

    def set_basic_salary(self, basic_salary):
        self.basic_salary = basic_salary

    def set_experience_years(self, experience_years):
        self.experience_years = experience_years

# Calculation of HRA, DA and PF
    def calculate_HRA(self):
        return self.basic_salary * 0.35

    def calculate_DA(self):
        return self.basic_salary * 0.58

    def calculate_PF(self):
        return self.basic_salary * 0.095

# Calculation of bonus based on years of experience 
    def calculate_bonus(self):
        if self.experience_years >= 30:
            return self.basic_salary * 0.59
        elif self.experience_years >= 23:
            return self.basic_salary * 0.51
        elif self.experience_years >= 15:
            return self.basic_salary * 0.45
        elif self.experience_years >= 7:
            return self.basic_salary * 0.33
        else:
            return self.basic_salary * 0.16

    def calculate_net_salary(self):
        return self.basic_salary + self.calculate_DA() + self.calculate_PF() + self.calculate_HRA() + self.calculate_bonus()

empid = int(input("Enter the employee ID : "))
name = input("Enter the name of the employee : ")
basic_salary = float(input("Enter the basic salary : "))
experience_years = float(input("Enter the years of experience : "))

employee = Employee(empid, name, basic_salary, experience_years)

print("Employee details : ")
print(name)
print(empid)
print(basic_salary)
print(experience_years)


print(employee.calculate_HRA())
print(employee.calculate_DA())
print(employee.calculate_PF())
print(employee.calculate_bonus())
print(employee.calculate_net_salary())