'''
（１）Hello!を10回表示するプログラムを作りなさい．
また，はじめのi=1をi=100にして，結果を出し，
そうなるわけを考察しなさい．
（２）20回表示するプログラムにしなさい
'''

def first():
    i = 1
    while i <= 10:
        print('Hello')
        i += 1
    print('終了')

def second():
    i = 1
    while i <= 20:
        print(f'{i}: hello')
        i += 1
    print('終了')


if __name__ == '__main__':
    first()
    second()
