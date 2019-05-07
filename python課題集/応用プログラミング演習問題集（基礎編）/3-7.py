'''
xとyにキーボードから整数を入力し，
その和差積を表示するようなプログラムを作りなさい．【やや難】
（ヒント：aの絶対値は abs(a) ）

'''
def main():
    x = int(input('x = '))
    y = int(input('y = '))
    print(f'和: {x + y}')
    print(f'差: {x - y}')
    print(f'積: {x * y}')


if __name__ == '__main__':
    main()
