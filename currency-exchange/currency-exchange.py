def main():
    while True:
        try:
            print("Please, enter the number of my_coins you have: ", end='')
            y = float(input('')) * float(input("Please, enter the exchange rate: "))
        except ValueError:
            print("ERROR")
        else:
            break
    print(f"The total amount of dollars: {round(y, 2)}")


if __name__ == "__main__":
    main()
