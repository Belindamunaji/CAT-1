class SalesPerson:
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales
        self.comm = 0
        self.bonus = 0
        self.tax = 0
        self.nssf = 0
        self.nhif = 0
        self.levy = 0
        self.rem = 0
        self.net = 0

    def calc_pay(self):
        if self.sales > 500000:
            self.comm = 0.3 * self.sales
            self.bonus = 25000
        elif self.sales >= 350000:
            self.comm = 0.2 * self.sales
        elif self.sales >= 200000:
            self.comm = 0.1 * self.sales
        elif self.sales >= 50000:
            self.comm = 0.05 * self.sales

        self.rem = self.comm + self.bonus
        self.tax = 0.15 * self.rem
        self.nssf = 0.06 * self.rem
        self.levy = 0.015 * self.rem
        self.nhif = self.calc_nhif()
        self.net = self.rem - (self.tax + self.nssf + self.levy + self.nhif)

    def calc_nhif(self):
        if self.rem <= 5999:
            return 150
        elif self.rem <= 7999:
            return 300
        elif self.rem <= 11999:
            return 400
        elif self.rem <= 14999:
            return 500
        elif self.rem <= 19999:
            return 600
        elif self.rem <= 24999:
            return 750
        elif self.rem <= 29999:
            return 850
        elif self.rem <= 34999:
            return 900
        elif self.rem <= 39999:
            return 950
        elif self.rem <= 44999:
            return 1000
        elif self.rem <= 49999:
            return 1100
        elif self.rem <= 59999:
            return 1200
        elif self.rem <= 69999:
            return 1300
        elif self.rem <= 79999:
            return 1400
        elif self.rem <= 89999:
            return 1500
        elif self.rem <= 99999:
            return 1600
        else:
            return 1700

    def show(self):
        print("Name:", self.name)
        print("Sales:", self.sales)
        print("Commission:", self.comm)
        print("Bonus:", self.bonus)
        print("Remuneration:", self.rem)
        print("Tax:", self.tax)
        print("NSSF:", self.nssf)
        print("NHIF:", self.nhif)
        print("Housing Levy:", self.levy)
        print("Net Pay:", self.net)
        print("-" * 30)

# list of workers
staff = [
    SalesPerson("Alvin", 500000),
    SalesPerson("Belinda", 8000000),
    SalesPerson("Luther", 450000),
    SalesPerson("Anita", 4560000)
]

t_comm = 0
t_bonus = 0
t_tax = 0
t_nssf = 0
t_nhif = 0
t_levy = 0
t_net = 0

for p in staff:
    p.calc_pay()
    p.show()
    t_comm += p.comm
    t_bonus += p.bonus
    t_tax += p.tax
    t_nssf += p.nssf
    t_nhif += p.nhif
    t_levy += p.levy
    t_net += p.net

print("\nSummary:")
print("Total Commission:", t_comm)
print("Total Bonus:", t_bonus)
print("Total Tax:", t_tax)
print("Total NSSF:", t_nssf)
print("Total NHIF:", t_nhif)
print("Total Levy:", t_levy)
print("Total Net Pay:", t_net)

