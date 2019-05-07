'''
問題６－８のプログラムを使って，1 から入力した数nまでの素数を表示するプログラムを作りなさい．
'''
import sympy


def main():
    check_input = int(input('調べたい素数の上限を入力してください > '))
    print(list(sympy.primerange(1, check_input)))
    
if __name__ == '__main__':
    main()
