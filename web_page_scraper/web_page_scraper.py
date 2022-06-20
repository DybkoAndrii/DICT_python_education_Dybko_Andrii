import requests


def main():
    url = input("Input the URL: ")
    res = requests.get(url)
    if 300 > int(res.status_code) >= 200:
        quote = res.json()
        if 'content' in quote:
            print(quote['content'])
        else:
            print("Invalid quote resource!")
    else:
        print("Invalid quote resource!")


if __name__ == '__main__':
    main()
