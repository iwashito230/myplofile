'''
この演習は、
ハングマン演習シリーズの3のパート1です。
他の演習は次のとおりです。パート2とパート3。

この課題では、
SOWPODS辞書の単語のリストからランダムな単語を選択する関数を作成します。
このファイルをダウンロードして、
Pythonコードと同じディレクトリに保存してください。
このファイルはPeter Scorbleトーナメントで使用される単語の辞書のPeter Norvigによる編集です。

ファイルの各行には1つの単語が含まれています。

ヒント：randomランダムな単語を選ぶためにPython ライブラリを使用してください。
'''
import random


def main():
    with open('sowpods.txt', 'r') as f:
        print(random.choice(f.read()))


if __name__ == '__main__':
    main()
