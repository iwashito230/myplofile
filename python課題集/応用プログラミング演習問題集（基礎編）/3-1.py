'''
inputが入力した数値を変数に代入している，ということを，プログラムを作って確認せよ．
代入された変数の値を表示すれば確認できるので，プログラムの基本的な構造は以下のようになる．
1. 変数xを宣言する
2. inputで変数xに整数を入力する
3. printで変数xの値を表示する

（１）上の構造どおりのプログラムを作れ
（２）変数xの名前を自分の好きな名前に変えてみよ．
（３）数値を入力して表示する，という作業を２回するようにしましょう．
（４）入力する前にseisuu = ?と表示するようにせよ．
（５）小数を入力し，それを表示させるように変えよ


'''
def first():
        x = input('(1) > ')
        print()

def second():
        n = int(input('(2) >'))
        print(n)

def third():
    for n in range(2):
        n = int(input('(3) >'))
        print(n)

def forth():
    for n in range(2):
        n = input('(4)seisuu = ')
        print(n)

def fifth():
    for n in range(2):
        n = input('(5)seisuu = ')
        print(n)


if __name__ == '__main__':
    first()
    second()
    third()
    forth()
    fifth()

