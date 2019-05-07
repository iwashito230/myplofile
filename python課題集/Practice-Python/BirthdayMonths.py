'''
この演習は、
誕生日データ演習シリーズの4のパート3です。
その他の演習は、パート1、パート2、およびパート4です。

で前の演習我々は、
ディスクに有名な科学者の名前や誕生日についての情報を保存しました。
この演習では、
そのJSONファイルをディスクからロードし、
すべての誕生日の月を抽出して、各月に何人の科学者が誕生日を過ごしたかを数えます。

あなたのプログラムは次のように出力されるはずです。

{
    "May": 3,
    "November": 2,
    "December": 1
}
'''
from collections import Counter
from datetime import datetime
import json


def main():
    month = []

    with open('b.json', 'r') as f:
        f = json.load(f)
        #jsonデータを必要なものだけ抽出
        birthmonth = [k['birthday'].split('/')[0] for k in f.get('person')]
        for b in birthmonth:
            dateConv = datetime.strptime(b, '%m')
            egBirthmonth = datetime.strftime(dateConv, '%B')
            month.append(egBirthmonth)

        print('登録されている人の誕生月は')
        print(Counter(month))


if __name__ == '__main__':
    main()
