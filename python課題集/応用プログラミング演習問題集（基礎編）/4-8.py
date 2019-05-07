'''
キーボードから数を入力し，その数が正ならその数を表示．
そうでなければ，もうひとつ数を入力し，最初の数との積を表示するプログラムを作りなさい．
表示結果例
x = :-3
y = :2
seki  -6
'''

def main():
    x = int(input('Please enter an integer: x = '))
    y = int(input('Please enter an integer: y = '))

    if x >= 0 and y >= 0:
        print(x)
        print(y)
    else:
        print(x * y)

if __name__ == '__main__':
    main()
