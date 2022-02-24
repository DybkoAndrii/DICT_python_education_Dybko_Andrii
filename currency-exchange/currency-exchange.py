import requests


def check_req(y, x):
    try:
        res = requests.get(f'http://www.floatrates.com/daily/{y}.json')
        qwe = res.json()
    except ValueError:
        print("ERROR")
        return "ERROR"
    else:
        return qwe[x]['rate']


def main():
    a = input("Enter your currency code: ")
    cache = {'USD': check_req(a, 'usd'), 'EUR': check_req(a, 'eur')}
    while True:
        b = input("Enter the code of the required currency: ")
        if b.lower() == "!exit":
            break
        while True:
            try:
                money = float(input("Enter the amount of money: "))
            except ValueError:
                print("ERROR")
            else:
                break
        print("Checking the cache...")
        if b.upper() in cache:
            print("It is in the cache!")
            print(f"You received {round(money * float(cache[b.upper()]), 2)} {b.upper()}")
        else:
            print("Sorry, but it is not in the cache!")
            cache[b.upper()] = check_req(a, b.lower())
            print(f"You received {round(money * float(cache[b.upper()]), 2)} {b.upper()}")


if __name__ == "__main__":
    main()
