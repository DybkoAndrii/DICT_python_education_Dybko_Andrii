def main():
    while True:
        try:
            y = float(input("Please, enter the number of my_coins you have: "))
        except ValueError:
            print("ERROR")
        else:
            break
    print(f"""I will get {round(y * 0.82, 2)} ARS from the sale of {y} my_coins.
I will get {round(y * 0.17, 2)} HNL from the sale of {y} my_coins.
I will get {round(y * 1.9622, 2)} AUD from the sale of {y} my_coins.
I will get {round(y * 0.208, 2)} MAD from the sale of {y} my_coins.""")


if __name__ == "__main__":
    main()
