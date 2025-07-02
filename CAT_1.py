class SalesPerson:
    def __init__(self, name, total_sales):
        self.name = name
        self.total_sales = total_sales
        self.commission = 0
        self.bonus = 0
        self.tax = 0
        self.nssf = 0
        self.nhif = 0
        self.housing_levy = 0
        self.remuneration = 0
        self.net_pay = 0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Total Sales: Ksh {self.total_sales}")
        print(f"Commission: Ksh {self.commission}")
        print(f"Bonus: Ksh {self.bonus}")
        print(f"Remuneration: Ksh {self.remuneration}")
        print(f"Tax (15%): Ksh {self.tax}")
        print(f"NSSF (6%): Ksh {self.nssf}")
        print(f"NHIF: Ksh {self.nhif}")
        print(f"Housing Levy (1.5%): Ksh {self.housing_levy}")
        print(f"Net Pay: Ksh {self.net_pay}")
        print("-" * 40)

    def calculate_remuneration(self):
        # Commission and bonus 
        if self.total_sales > 500000:
            self.commission = 0.3 * self.total_sales
            self.bonus = 25000
        elif 350000 <= self.total_sales <= 499999:
            self.commission = 0.2 * self.total_sales
        elif 200000 <= self.total_sales <= 349999:
            self.commission = 0.1 * self.total_sales
        elif 50000 <= self.total_sales <= 199999:
            self.commission = 0.05 * self.total_sales
        else:
            self.commission = 0
            self.bonus = 0

        self.remuneration = self.commission + self.bonus

        # Deductions
        self.tax = 0.15 * self.remuneration
        self.nssf = 0.06 * self.remuneration
        self.housing_levy = 0.015 * self.remuneration
        self.nhif = self.calculate_nhif()

        # Net Pay
        self.net_pay = self.remuneration - (self.tax + self.nssf + self.nhif + self.housing_levy)

    def calculate_nhif(self):
        # Simplified NHIF based on gross salary (remuneration)
        if self.remuneration <= 5999:
            return 150
        elif self.remuneration <= 7999:
            return 300
        elif self.remuneration <= 11999:
            return 400
        elif self.remuneration <= 14999:
            return 500
        elif self.remuneration <= 19999:
            return 600
        elif self.remuneration <= 24999:
            return 750
        elif self.remuneration <= 29999:
            return 850
        elif self.remuneration <= 34999:
            return 900
        elif self.remuneration <= 39999:
            return 950
        elif self.remuneration <= 44999:
            return 1000
        elif self.remuneration <= 49999:
            return 1100
        elif self.remuneration <= 59999:
            return 1200
        elif self.remuneration <= 69999:
            return 1300
        elif self.remuneration <= 79999:
            return 1400
        elif self.remuneration <= 89999:
            return 1500
        elif self.remuneration <= 99999:
            return 1600
        else:
            return 1700


# List of salespeople
salespeople = [
    SalesPerson("Alvin", 500000),
    SalesPerson("Belinda", 8000000),
    SalesPerson("Luther", 450000),
    SalesPerson("Anita", 4560000),
    SalesPerson("Ida", 300000),
    SalesPerson("Josephine", 150000),
    SalesPerson("Brown", 100000),
    SalesPerson("Cole", 700000),
    SalesPerson("Betty", 200000),
    SalesPerson("Shadrack", 10000),
    SalesPerson("Joyce", 850000),
    SalesPerson("Mary", 360000),
    SalesPerson("Marion", 520000),
    SalesPerson("Sharon", 180000),
    SalesPerson("Lucy", 270000),
    SalesPerson("Munaji", 460000),
    SalesPerson("Teicy", 250000),
    SalesPerson("Abdul", 320000),
    SalesPerson("Kodhek", 400000),
    SalesPerson("Shanice", 510000)
]

# Totals
total_commission = 0
total_bonus = 0
total_tax = 0
total_nssf = 0
total_nhif = 0
total_housing_levy = 0
total_net_pay = 0

for person in salespeople:
    person.calculate_remuneration()
    person.display_info()
    total_commission += person.commission
    total_bonus += person.bonus
    total_tax += person.tax
    total_nssf += person.nssf
    total_nhif += person.nhif
    total_housing_levy += person.housing_levy
    total_net_pay += person.net_pay

# Summary
print("\n====== SUMMARY ======")
print(f"Total Commission: Ksh {total_commission}")
print(f"Total Bonus: Ksh {total_bonus}")
print(f"Total Tax: Ksh {total_tax}")
print(f"Total NSSF: Ksh {total_nssf}")
print(f"Total NHIF: Ksh {total_nhif}")
print(f"Total Housing Levy: Ksh {total_housing_levy}")
print(f"Total Net Pay: Ksh {total_net_pay}")

