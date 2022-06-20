import requests


def save_html(html):
    with open("source.html", "wb") as f:
        f.write(html)


def main():
    url = input("Input the URL: ")
    res = requests.get(url)
    if res.status_code == 200:
        html = res.content
        save_html(html)
        print("Content saved")
    else:
        print(f"The URL returned {res.status_code}!")


if __name__ == '__main__':
    main()
