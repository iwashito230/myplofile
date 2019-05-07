'''
ユーザーに自分の名前と年齢を入力するように求めるプログラムを作成します。
彼らに宛てたメッセージを印刷して、彼らに100歳になるという年を伝えます。

'''
import datetime


def main():
    user_name = input('あなたのお名前なんですか？? > ')
    user_age = int(input('年齢はいくつですか？ > '))
    age_100 = int(datetime.datetime.now().strftime('%Y')) + (100 - user_age)
    print(f'{user_name}さんが100歳になるのは{age_100}年です')


if __name__ == '__main__':
    main()
