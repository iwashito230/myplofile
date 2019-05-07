'''
1,2,3章で勉強したinput，print，変数の3つだけで
借金返済計画を立てるプログラムを作りたい．
簡単のため，利子は無しとする．
まず，借金の総額と，ひと月に返済する金額を入力すると，
返済にかかる年数を表示し，
さらに，毎年のボーナスから返済する金額を入力すると，
返済完了が何年早まるかを表示し，
その次に返済を完了したい年数を入力すると，
ボーナスからいくら返せばよいかを表示するプログラムを作成せよ．

'''

def main():
    debt = int(input('借金総額 > '))
    repayment = int(input('返済額 > '))
    n_period = debt / repayment
    print(f'返済にかかる年数は round({n_period/ 12}) です。')

    if input('ボーナスも追加しますか？ > ') == 'y':
        bonus = int(input('ボーナス月返済額 >'))
        year = repayment * 10 + bonus * 2
        b_period = n_period - round((debt / year), 1)
        print(f'{round(b_period, 1)}年早まりました')

    if input('返却完了年数でシュミレーションしますか？ > ') == 'y':
        comp = input('返却完了年数 > ')
        print(f'毎月{round(debt / int(comp))}円')


if __name__ == '__main__':
      main()
