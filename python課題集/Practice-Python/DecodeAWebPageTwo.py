'''
requestsおよびBeautifulSoupPythonライブラリを使用して、
このWebサイトの記事の全文を画面に印刷します。

http : //www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture。

記事は長いので、4ページに分かれています。
あなたの仕事はあなたがどんなボタンもクリックする必要なしに
全文を読むことができるようにスクリーンに
テキストをプリントアウトすることです。

（ヒント：ここの投稿では、
ここで投稿された演習の解決方法で
BeautifulSoupand requestsライブラリを使用する方法について
詳しく説明しています。）

これは記事の全文をスクリーンに表示するだけです。
読みにくくはないので、
次の課題ではこのテキストを.txtファイルに書き込む方法を学びます。

'''


from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
    soup = BeautifulSoup(response.text, 'html.parser')
    NewsContents = soup.select('section.content-section > p').get('data-reactid')

    for section in NewsContents:
        print(section, end='')


if __name__ == '__main__':
    main()
