def help_(qwe):
    print(f"""Available formatters: {qwe}
Special commands: !help !done""")


def save():
    pass


def main():
    choices = ("plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line")
    while True:
        action = input("Choose a formatter: ")
        if action == "!help":
            help_(choices)
        elif action in choices:
            pass
        elif action == "!done":
            save()
            break
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
