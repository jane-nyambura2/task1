payroll_no = input("Enter Payroll Number: ")
name = input("Enter Employee Name: ")
gender = input("Enter Gender (M/F): ")
job_group = input("Enter Job Group (J, K, L, M): ").upper()
basic_salary = float(input("Enter Basic Salary (KES): "))


if job_group == "J":
    allowance = 5000
elif job_group == "K":
    allowance = 5500
elif job_group == "L":
    allowance = 6000
elif job_group == "M":
    allowance = 6500
else:
    allowance = 0
    print("Invalid Job Group! No allowance added.")

gross_pay = basic_salary + allowance
taxes = 0.12 * basic_salary
net_pay = gross_pay - taxes


print("\n--- EMPLOYEE PAYSLIP ---")
print(f"Payroll Number: {payroll_no}")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Job Group: {job_group}")
print(f"Basic Salary: KES {basic_salary:.2f}")
print(f"House Allowance: KES {allowance:.2f}")
print(f"Gross Pay: KES {gross_pay:.2f}")
print(f"Taxes (12%): KES {taxes:.2f}")
print(f"Net Pay: KES {net_pay:.2f}")