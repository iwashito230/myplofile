'''
3つの変数を入力として受け取り、
3つのうち最大のものを返す関数を実装します。
Python max()関数を使用せずにこれを実行してください。

この課題の目標は、
Pythonが通常私たちの面倒をみるいくつかの内部構造について考えることです。

必要なのは、いくつかの変数とif文だけです。
'''

def main():
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    number = {'a': a, 'b': b, 'c': c}
    desc = sorted(number.values(), key=lambda x: -x)
    print(f'{desc[0]}が最大')


if __name__ == '__main__':
    main()
