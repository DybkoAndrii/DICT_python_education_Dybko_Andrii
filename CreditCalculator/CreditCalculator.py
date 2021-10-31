import math


def n_of_mp():
    p = int(input("Enter the loan principal: "))
    a = int(input("Enter the monthly payment: "))
    ni = int(input("Enter the loan interest: "))
    i = ni / 1200
    n = math.log(a / (a - i * p), 1 + i)
    n_n2 = n.__ceil__() % 12
    n_n1 = int((n.__ceil__() - n_n2) / 12)
    if n_n2 == 0:
        print("It will take " + str(n_n1) + " years")
    else:
        print("It will take " + str(n_n1) + " years and " + str(n_n2) + " months to repay this loan!")


def am_pa():
    p = int(input("Enter the loan principal: "))
    n_n = int(input("Enter the number of periods: "))
    ni = int(input("Enter the loan interest: "))
    i = ni / 1200
    a = (p * i * (1 + i) ** n_n) / (((i + 1) ** n_n) - 1)
    print("Your monthly payment = " + str(a.__ceil__()) + " !")


def for_lnp():
    a = float(input("Enter the annuity payment: "))
    n_n = float(input("Enter the number of periods: "))
    ni = float(input("Enter the loan interest: "))
    i = ni / 1200
    p = a / ((i * (1 + i) ** n_n) / (((i + 1) ** n_n) - 1))
    print("Your loan principal = " + str(int(p)) + " !")


action = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: """)
if action == "n":
    n_of_mp()
elif action == "a":
    am_pa()
elif action == "p":
    for_lnp()
