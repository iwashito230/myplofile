'''
（１）「入力した数が7の倍数かどうかを判定する」という作業を繰り返す
プログラムを作りなさい．
（２）３の倍数かどうかの判定を繰り返すようにせよ
（３）負かどうかの判定を繰り返すようにせよ
'''

def first():
    while True:
        i = int(input('please enter an integer > '))
        if i != 0 and i % 7 == 0:
            print('7の倍数です、処理を終了します')
            break

def second():
    while True:
        i = int(input('please enter an integer > '))
        if i != 0 and i % 3 == 0:
            print('3の倍数です、処理を終了します')
            break

def third():
    while True:
        i = int(input('please enter an integer > '))
        if i < 0:
            print('Wow mainasu!')
            break


if __name__ == '__main__':
    first()
    second()
    third()
