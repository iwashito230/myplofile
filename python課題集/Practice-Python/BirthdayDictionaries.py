'''
この演習は、誕生日データ演習シリーズの4のパート1です。
その他の演習は、パート2、パート3、およびパート4です。

この演習では、
友人の誕生日がいつであるかを追跡し、
名前に基づいてその情報を見つけることができます。

名前と誕生日の辞書を（あなたのファイルの中に）作成してください。

あなたがプログラムを実行するとき、
それはユーザに名前を入力するように頼み、
そしてその人の誕生日を彼らに返すべきです。対話は次のようになります。

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.

'''
def main():
    birthday = {
      'Benjamin Franklin': '01/17/1706',
      'Albert Einstein ': '03/14/1879',
      'Ada Lovelace': '12/10/1815',
      }

    print('\t誕生日を知っています。誕生日辞書へようこそ')
    print('>>> Welcome to the birthday dictionary. We know the birthdays of: ')

    for key in birthday.keys():
        print(key)

    print('\t誰の誕生日を見たいですか？')
    print(">>> Who's birthday do you want to look up?")
    user = input('> ')

    if user in birthday.keys():
        print(f"{user}'s birthday is {birthday[user]}")
    else:
        print('その人は登録されていません！')


if __name__ == '__main__':
    main()
