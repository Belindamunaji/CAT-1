salaries = []
net_salaries = []
taxes = []

try:
    count = int(input("How many salaries do you want to enter? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

for i in range(count):
    try:
        salary = int(input(f"Enter salary #{i+1}: "))
    except ValueError:
        print("Invalid input. Skipping this entry.")
        continue

    if salary >= 500000:
        tax_rate = 0.4
    elif salary >= 300000:
        tax_rate = 0.35
    elif salary >= 100000:
        tax_rate = 0.3
    elif salary >= 50000:
        tax_rate = 0.25
    elif salary >= 10000:
        tax_rate = 0.2
    else:
        tax_rate = 0

    tax = salary * tax_rate
    net_income = salary - tax

    salaries.append(salary)
    taxes.append(tax)
    net_salaries.append(net_income)

    print(f"Net Salary: {net_income:.2f} | Tax: {tax:.2f}")

if salaries:
    print("\n--- Taxation Summary ---")
    print(f"Total salaries processed: {len(salaries)}")
    print(f"Total tax collected: {sum(taxes):.2f}")
    print(f"Average salary: {sum(salaries)/len(salaries):.2f}")
    print(f"Highest salary: {max(salaries)}")
    print(f"Lowest salary: {min(salaries)}")
    print("Thank you for using the iTax System.")
else:
    print("No valid salaries were entered.")

