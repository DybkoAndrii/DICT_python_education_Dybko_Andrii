import requests
from os import mkdir
from bs4 import BeautifulSoup as Bs


def save_articles(content):
    for i in content.keys():
        mkdir(f'Page_{i}')
        for j in content[i].keys():
            with open(f"Page_{i}/{j}.txt", "w", encoding='utf-8') as f:
                for k in content[i][j]:
                    f.writelines(k)


def transform_txt(txt):
    trans = txt.maketrans(' -,.?!<>"/|+=*', '______________')
    return txt.translate(trans)


def user_inp():
    while True:
        try:
            number = int(input('number of pages: ').strip())
        except ValueError:
            print('Only numerical values')
        else:
            break
    types_arts = ['Comment', 'News & Views', 'Outlook', 'News Feature', 'News', 'Article', 'Nature Briefing',
                  'Author Correction', 'Career Column', 'Career Feature', 'Correspondence',
                  'Editorial', 'Futures', 'Matters Arising', 'Nature Podcast', 'Publisher Correction',
                  'Research Briefing', 'Research Highlights', 'Where I Work', 'World View']
    while True:
        type_art = input('article type: ')
        if type_art in types_arts:
            break
        else:
            print('non-existent type')
            print(types_arts)
    return number, type_art


def news(direct):
    for i in direct.keys():
        articles = {}
        for j in range(len(direct[i])):
            qwe = requests.get(direct[i][j])
            soup = Bs(qwe.content, 'html.parser')
            try:
                header = transform_txt(soup.find('h1', class_='c-article-magazine-title').text)
            except AttributeError:
                try:
                    header = transform_txt(soup.find(class_='Theme-StoryTitle Theme-TextSize-small h-align-right').text)
                except AttributeError:
                    header = transform_txt(soup.find(class_='Theme-StoryTitle Theme-TextSize-xsmall').text)
            try:
                text = [k.text for k in soup.find('div', class_='c-article-body u-clearfix').find_all('p')]
            except AttributeError:
                text = [k.text for k in soup.find(class_='Core--rootElement Theme-Story').find_all('p')]
            articles[header] = text
        direct[i] = articles
    return direct


def research(direct):
    for i in direct.keys():
        articles = {}
        for j in range(len(direct[i])):
            qwe = requests.get(direct[i][j])
            soup = Bs(qwe.content, 'html.parser')
            header = transform_txt(soup.find(class_='c-article-magazine-title').text)
            text = [soup.find("p", class_="article__teaser").text]
            articles[header] = text
        direct[i] = articles
    return direct


def article(direct):
    for i in direct.keys():
        articles = {}
        for j in range(len(direct[i])):
            qwe = requests.get(direct[i][j])
            soup = Bs(qwe.content, 'html.parser')
            header = transform_txt(soup.find(class_='c-article-title').text)
            text = [k.text for k in soup.find('div', class_='c-article-section__content').find_all('p')]
            articles[header] = text
        direct[i] = articles
    return direct


def get_links(url, type_art):
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
        if types_s[i] == type_art:
            links_news.append(re[i])
    return links_news


def main():
    number, type_art = user_inp()
    links = []
    for i in range(1, number+1):
        links.append(get_links(f'https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={i}', type_art))
    direct = {}
    num = 0
    for i in range(len(links)):
        if len(links[i]) > 0:
            direct[i+1] = links[i]
            num += 1
    if num > 0:
        if type_art == 'Comment':
            news(direct)
        elif type_art == 'News & Views':
            research(direct)
        elif type_art == 'Outlook':
            news(direct)
        elif type_art == 'News Feature':
            news(direct)
        elif type_art == 'News':
            news(direct)
        elif type_art == 'Article':
            article(direct)
        elif type_art == 'Nature Briefing':
            news(direct)
        elif type_art == 'Author Correction':
            article(direct)
        elif type_art == 'Career Column':
            news(direct)
        elif type_art == 'Career Feature':
            news(direct)
        elif type_art == 'Correspondence':
            research(direct)
        elif type_art == 'Editorial':
            news(direct)
        elif type_art == 'Futures':
            news(direct)
        elif type_art == 'Matters Arising':
            article(direct)
        elif type_art == 'Nature Podcast':
            news(direct)
        elif type_art == 'Publisher Correction':
            article(direct)
        elif type_art == 'Research Briefing':
            research(direct)
        elif type_art == 'Research Highlights':
            research(direct)
        elif type_art == 'Where I Work':
            news(direct)
        else:
            news(direct)
        save_articles(direct)
        print('Saved all articles')
    else:
        print('there are no articles of this type on the entered pages')


if __name__ == '__main__':
    main()
