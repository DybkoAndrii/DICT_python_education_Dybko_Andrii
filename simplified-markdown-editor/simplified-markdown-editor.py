def save(mkd):
    with open("output.md", "w") as f:
        f.write(mkd)


def edit(qwe):
    md_st = ""
    if qwe == "plain":
        md_st += f"{input('Text: ')} "
    elif qwe == "bold":
        md_st += f"**{input('Text: ')}** "
    elif qwe == "italic":
        md_st += f"*{input('Text: ')}* "
    elif qwe == "header":
        while True:
            try:
                lvl = int(input("Level: "))
                if 0 < lvl < 7:
                    md_st += f"{'#' * lvl} {input('Text: ')}\n"
                else:
                    print("The level should be within the range of 1 to 6")
                    continue
            except ValueError:
                print("Enter a numeric value")
            else:
                break
    elif qwe == "link":
        md_st += f"[{input('Label: ')}]({input('Url: ')}) "
    elif qwe == "inline-code":
        md_st += f"`{input('Code: ')}` "
    elif qwe == "ordered-list":
        while True:
            try:
                rw = int(input("Number of rows: "))
                if rw > 0:
                    for i in range(rw):
                        md_st += f"{i + 1}. {input(f'Row #{i + 1}: ')}\n"
                else:
                    print("The number of rows should be greater than zero")
                    continue
            except ValueError:
                print("Enter a numeric value")
            else:
                break
    elif qwe == "unordered-list":
        while True:
            try:
                rw = int(input("Number of rows: "))
                if rw > 0:
                    for i in range(rw):
                        md_st += f"* {input(f'Row #{i + 1}: ')}\n"
                else:
                    print("The number of rows should be greater than zero")
                    continue
            except ValueError:
                print("Enter a numeric value")
            else:
                break
    elif qwe == "new-line":
        md_st += " \n"
    return md_st


def main():
    choices = ("plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line")
    markdown = ""
    while True:
        action = input("Choose a formatter: ")
        if action == "!help":
            print(f"""Available formatters: {choices}
Special commands: !help !done""")
        elif action in choices:
            markdown += edit(action)
            print(markdown)
        elif action == "!done":
            save(markdown)
            break
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
