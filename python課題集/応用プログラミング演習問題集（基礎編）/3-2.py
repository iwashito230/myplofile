'''
入力した数値を使った計算をする．inputを使ってキーボードから２つの整数を入力して，その合計を表示する，というプログラムを作りたい．
プログラムの基本的な構造は以下のようになる．
1. 整数変数を2つ宣言する
2. 整数を2つ入力し，宣言した変数に代入する
3. 2つの整数の和を表示する

（１）上の構造どおりのプログラムを作れ
（２）整数３つを入力して，その合計を表示するようにせよ
（３）小数２つを入力して，その合計を表示するようにせよ
（４）整数２つを入力して，その積を表示するようにせよ

'''

def first():
    x = 12
    y = 32
    total = x + y
    print(total)

def second():
    x = 12
    y = 32
    z = 2
    total = x + y + z
    print(total)

def third():
    x = 1.2
    y = 3.2
    total = x + y
    print(total)

def forth():
    x = 12
    y = 32
    total = x * y
    print(total)


if __name__ == '__main__':
    first()
    second()
    third()
    forth()
