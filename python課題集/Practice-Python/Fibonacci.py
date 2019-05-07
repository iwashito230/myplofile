'''
ユーザーにいくつのFibonnaci番号を生成し、
次にそれらを生成するかを尋ねるプログラムを書く。
この機会を利用して、関数の使い方を考えてみましょう。
生成するシーケンス内の数字の数を入力するようにユーザーに依頼してください
（ヒント：
シーケンス内の次の数字がシーケンス内の前の2つの数字の合計となる数字のシーケンスです。
シーケンス1、1、2、3、5、8、13、…）
'''
import sympy


def main():
    max_number = int(input('フィボナッチをいくつまで生成しますか？ > '))
    print([sympy.fibonacci(num) for num in range(max_number)])


if __name__ == '__main__':
    main()
