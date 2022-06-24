import requests
from bs4 import BeautifulSoup as Bs


def save_articles(content):
    for i in content.keys():
        with open(f"{i}.txt", "w", encoding='utf-8') as f:
            for j in content[i]:
                f.writelines(j)


def main():
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3'
    res = requests.get(url)
    cont = Bs(res.content, 'html.parser')
    type_ls = cont.find_all('span', class_='c-meta__type')
    types_s = []
    for i in type_ls:
        types_s.append(i.text)
    refs = cont.find_all('a', class_='c-card__link u-link-inherit')
    re = []
    for i in refs:
        re.append('https://www.nature.com' + i.get('href'))
    links_news = []
    for i in range(len(types_s)):
        if types_s[i] == 'News':
            links_news.append(re[i])
    articles = {}
    for i in links_news:
        qwe = requests.get(i)
        soup = Bs(qwe.content, 'html.parser')
        header = soup.find('h1', class_='c-article-magazine-title').text
        trans = header.maketrans(' -,.?!', '______')
        hea_der = header.translate(trans)
        text = []
        for j in soup.find('div', class_='c-article-body u-clearfix').find_all('p'):
            text.append(j.text)
        articles[hea_der] = text
    save_articles(articles)
    print('Saved:')
    for i in articles.keys():
        print(f'{i}.txt')


if __name__ == '__main__':
    main()
