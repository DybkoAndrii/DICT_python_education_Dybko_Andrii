import math
import argparse
calculator = argparse.ArgumentParser()
calculator.add_argument("--type")
calculator.add_argument("--principal", type=float)
calculator.add_argument("--periods", type=int)
calculator.add_argument("--interest", type=float)
calculator.add_argument("--payment", type=float)
args = calculator.parse_args()


def n_of_mp():
    p = args.principal
    a = args.payment
    li = args.interest
    i = li / 1200
    n = math.log(a / (a - i * p), 1 + i)
    n_n2 = n.__ceil__() % 12
    n_n1 = int((n.__ceil__() - n_n2) / 12)
    if n_n2 == 0:
        print("It will take " + str(n_n1) + " years")
    else:
        print("It will take " + str(n_n1) + " years and " + str(n_n2) + " months to repay this loan!")
    print("")
    m = 0
    abc = 0
    for y in range(n.__ceil__()):
        m += 1
        d = p / n.__ceil__() + i * (p - (p * (m - 1)) / n.__ceil__())
        abc += d
    overpayment = abc - p
    print("Overpayment = {}".format(overpayment.__ceil__()))


def am_pa():
    p = args.principal
    n_n = args.periods
    li = args.interest
    i = li / 1200
    a = (p * i * (1 + i) ** n_n) / (((i + 1) ** n_n) - 1)
    print("Your monthly payment = " + str(a.__ceil__()) + " !")
    print("")
    m = 0
    abc = 0
    for y in range(n_n):
        m += 1
        d = p / n_n + i * (p - (p * (m - 1)) / n_n)
        abc += d
    overpayment = abc - p
    print("Overpayment = {}".format(overpayment.__ceil__()))


def for_lnp():
    a = args.payment
    n_n = args.periods
    li = args.interest
    i = li / 1200
    p = a / ((i * (1 + i) ** n_n) / (((i + 1) ** n_n) - 1))
    print("Your loan principal = " + str(int(p)) + " !")
    print("")
    m = 0
    abc = 0
    for y in range(n_n):
        m += 1
        d = p / n_n + i * (p - (p * (m - 1)) / n_n)
        abc += d
    overpayment = abc - p
    print("Overpayment = {}".format(overpayment.__ceil__()))


def dif_f():
    p = args.principal
    n_n = args.periods
    li = args.interest
    i = li / 1200
    m = 0
    abc = 0
    for x in range(n_n):
        m += 1
        d = p / n_n + i * (p - (p * (m - 1)) / n_n)
        abc += d
        print("Month {}: payment is {}".format(m, d.__ceil__()))
    overpayment = abc - p
    print("")
    print("Overpayment = {}".format(overpayment.__ceil__()))


action = args.type
if args.type:
    if action == "annuity":
        if args.principal and args.payment and args.interest:
            if args.principal > 0 and args.payment > 0 and args.interest > 0:
                n_of_mp()
            else:
                print("Incorrect parameters")
        elif args.principal and args.periods and args.interest:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                am_pa()
            else:
                print("Incorrect parameters")
        elif args.payment and args.periods and args.interest:
            if args.payment > 0 and args.periods > 0 and args.interest > 0:
                for_lnp()
            else:
                print("Incorrect parameters")
        else:
            print("Incorrect parameters")
    elif action == "diff":
        if args.principal and args.periods and args.interest:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                dif_f()
            else:
                print("Incorrect parameters")
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
