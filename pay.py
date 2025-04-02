class Employee:
    def __init__(self, emp_id, name, basic_salary, tax_rate, bonus=0):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
        self.tax_rate = tax_rate
        self.bonus = bonus

    def calculate_net_salary(self):
        tax_deduction = self.basic_salary * self.tax_rate
        net_salary = self.basic_salary - tax_deduction + self.bonus
        return net_salary

    def generate_payslip(self):
        payslip = f"""
============================
Employee ID: {self.emp_id}
Name: {self.name}
Basic Salary: {self.basic_salary}
Tax Deduction: {self.basic_salary * self.tax_rate}
Bonus: {self.bonus}
Net Salary: {self.calculate_net_salary()}
============================
        """
        return payslip

def main():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    tax_rate = float(input("Enter Tax Rate (as a decimal): "))
    bonus = float(input("Enter Bonus (optional, default is 0): ") or 0)

    employee = Employee(emp_id, name, basic_salary, tax_rate, bonus)
    print(employee.generate_payslip())

if __name__ == "__main__":
    main()
