'''
Webサイトのデコード方法の演習からコードを取得し
（それをしなかった場合、
または単に別のコードでプレイしたい場合は、
ソリューションのコードを使用します）、
結果を画面に印刷する代わりに結果を書きます。 

TXTファイルに。
あなたのコードでは、あなたが保存しているファイルの名前を作るだけです。

補足：

保存する出力ファイルの名前を指定するようにユーザーに依頼してください。

'''
from bs4 import BeautifulSoup
import os
import requests


def main():
    resp = requests.get('https://www.nytimes.com/')
    soup = BeautifulSoup(resp.text, 'html.parser')
    NewsTitles = soup.select('div.css-1vynn0q > h2 > span')

    filename = input('取得したデータを保存する先の名前は？ > ')

    with open(filename, 'w', encoding='utf-8') as f:
        for title in NewsTitles:
            f.write(f'{title}')
        print('上記の内容を保存')


if __name__ == '__main__':
    main()
