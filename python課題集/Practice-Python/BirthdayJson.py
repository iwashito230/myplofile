'''
この演習は、誕生日データ演習シリーズの4のパート2です。
その他の演習は、パート1、パート3、およびパート4です。
で前の演習我々は、
有名な科学者の誕生日の辞書を作成しました。
この演習では、プログラムで辞書を定義するのではなく、
ディスク上のJSONファイルから
誕生日辞書をロードするようにパート1のプログラムを変更します。
ボーナス：
辞書に追加するために他の科学者の名前と誕生日をユーザに尋ねて、
あなたが科学者の名前で
あなたがディスクに持っているJSONファイルを更新する。
プログラムを複数回実行し、新しい名前を追加し続けると、
JSONファイルのサイズが大きくなっていくはずです。
'''
import json


def main():
    with open('b.json', 'r') as f:
        f = json.load(f)
        #jsonデータを必要なものだけ抽出
        birthday = {k['name']: k['birthday'] for k in f.get('person')}

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

            while True:
                anther = input('新しく登録しますか？ y or n > ')
                if anther == 'y':
                    print(f'{user}の生年月日を入れてください > ')
                    addBirth = input('dd/mm/yyyy > ')
                    newPerson = {"person": f['person'] + [{"name": user, "birthday": addBirth}]}
                    with open('b.json', 'w') as file:
                        file = json.dump(newPerson, file, ensure_ascii=False, indent=4)
                    main()
                    break
                elif anther == 'n':
                    break
                else:
                    print('y or nで選択 > ')
                    continue


if __name__ == '__main__':
    main()
