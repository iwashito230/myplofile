'''
整数を2つ入力して，それらの積を表示し，
さらに整数を2つ入力してそれらの積を表示し，
最後に，今までに表示した2つの数の合計を表示するプログラムを作りなさい．
例えば，プログラムを実行して10,20,33,30 を入力すると，
実行結果が以下のようになるようにします.
'''
import functools
import operator


def main():
    num = [int(input('>')) for i in range(2)]
    print(f'seki = {functools.reduce(operator.mul, num, 1)}')
    addnum = [int(input('>')) for i in range(2)]
    print(f'goukei = {sum(num + addnum)}')


if __name__ == '__main__':
    main()
