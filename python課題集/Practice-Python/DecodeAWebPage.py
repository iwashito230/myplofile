'''BeautifulSoupとrequestsPythonパッケージを使用して、
New York Timesのホームページにすべての記事のタイトルのリストを印刷してください。
https://www.nytimes.com/

'''
from bs4 import BeautifulSoup
import requests


def main():
    resp = requests.get('https://www.nytimes.com/')
    soup = BeautifulSoup(resp.text, 'html.parser')
    NewsTitles = soup.select('div.css-1vynn0q > h2 > span')

    for title in NewsTitles:
        print(title, end='\n')


if __name__ == '__main__':
    main()
