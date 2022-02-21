import requests


def main():
    while True:
        try:
            y = input("Please enter currency code: ")
            res = requests.get(f'http://www.floatrates.com/daily/{y}.json')
            qwe = res.json()
        except ValueError:
            print("ERROR")
        else:
            break
    print(f"""USD: {qwe['usd']['rate']}
EUR: {qwe['eur']['rate']}""")


if __name__ == "__main__":
    main()
