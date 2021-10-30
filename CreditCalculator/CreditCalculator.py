principal = int(input("Enter the loan principal: "))


def pay_men_t():
    month = int(input("Enter the number of months: "))
    qwe = principal / month
    payment = qwe.__ceil__()
    last_payment = principal - (month - 1) * payment
    if last_payment == payment:
        print("")
        print("Your monthly payment = " + str(payment))
    else:
        print("")
        print("Your monthly payment = " + str(payment) + " and the last payment = " + str(last_payment) + ".")


def n_payments():
    nam = int(input("Enter the monthly payment: "))
    qwe1 = principal / nam
    months = qwe1.__ceil__()
    print("")
    print("It will take " + str(months) + " months to repay the loan")


action = input("""What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment: """)
if action == "p":
    pay_men_t()
elif action == "m":
    n_payments()
