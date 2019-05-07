'''
キーボードから2つの数xとyを入力し，yがx以下ならx-yを表示し，
yがxより大きければminus ni narimasuと表示するプログラムを作りなさい．
'''

def main():
    x = int(input('Please enter an integer: x = '))
    y = int(input('Please enter an integer: y = '))

    if x >= y:
        print(x - y)
    elif x <= y:
        print('minus ni narimasu')


if __name__ == '__main__':
    main()
