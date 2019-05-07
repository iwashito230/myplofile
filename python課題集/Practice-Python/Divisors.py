'''
ユーザーに番号を要求してから、
その番号のすべての約数のリストを出力するプログラムを作成します。
（除数が何であるかがわからなければ、それは他の数に均等に分割する数です。
例えば、26/13には余りがないので、13は26の約数です。）

'''
import sympy


def main():
    num = int(input('番号を入れてください > '))
    print(sympy.divisors(num, generator=False))


if __name__ == '__main__':
    main()
