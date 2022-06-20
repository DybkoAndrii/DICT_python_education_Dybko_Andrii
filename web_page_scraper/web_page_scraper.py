import requests
from bs4 import BeautifulSoup as Bs


def main():
    url = input("Input the URL: ")
    if 'title' in url.split('/') and 'imdb' in url.split('.'):
        res = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
        if int(res.status_code) == 200:
            quote = Bs(res.text, 'html.parser')
            print(quote.find('title'))
            print('='*70)
            print(quote.find('meta', {'name': 'description'}, ['content']))
        else:
            print("Invalid quote resource!")
    else:
        print("Invalid quote resource!")


if __name__ == '__main__':
    main()
