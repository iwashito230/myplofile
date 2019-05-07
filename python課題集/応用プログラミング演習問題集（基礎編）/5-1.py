'''
（while文）（▲参考：例題５－１，５－２，例題５－３）
（１）「入力した数を表示する」という作業を，無条件に繰り返す
プログラムを作りなさい．
（２）「２つの数を入力し，表示する」という作業を繰り返すようにせよ．
（３）「入力した定価の税込価格を表示する」という作業を
繰り返すプログラムを作成せよ．
（４）０を入力したら止まるプログラムにせよ
（５）負の数を入力したら止まるプログラムにせよ

'''

def first():
    i = int(input('please enter an integer > '))
    while i:
        print(i)
        break

def second():
    x = int(input('Please enter an integer x = '))
    y = int(input('Please enter an integer y = '))

    while x == y:
        print(f'{x}, {y}')
        break

def third():
    i = int(input('please enter an integer > '))

    while i:
        print(f'税込 {i * 1.08}円')
        break

def forth():

    while True:
        i = int(input('please enter an integer > '))
        if i == 0:
            print('処理を終了します')
            break

def fifth():

    while True:
        i = int(input('please enter an integer > '))
        if i < 0:
            print('処理を終了します')
            break


if __name__ == '__main__':
    first()
    second()
    third()
    forth()
    fifth()
