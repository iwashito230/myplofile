'''
（１）「数を10回入力して表示する，
ただし，途中で0が入力されたら終了する」プログラムを作れ．
（２）「数を20回入力するようにせよ
（３）100を入力したら終わるようにせよ．
（４）負の数を入力したら終わるようにせよ．
（５）0か1を入力したら終わるようにせよ．
（６）「入力した数を表示する作業を，0が入力されるまで繰り返す，
ただし，10回を過ぎたら終了する」プログラムをfor文を用いて作れ
'''

def first():
    n = 1
    while True:
        i = int(input('数字いれてね > '))
        n += 1
        if i == 0:
            print('処理を終了します')
            break
        elif n > 10:
            break

def second():
    n = 1
    while True:
        i = int(input('数字をいれてね > '))
        n += 1
        if n > 20:
            break

def third():
    while True:
        i = int(input('数字いれてね > '))
        if i == 100:
            print('100を入力したので、処理を終了します')
            break

def fourth():
    while True:
        i = int(input('数字いれる >'))
        if i <= 0:
            print('負の数なので、処理を終了します')
            break

def fifth():
    while True:
        i = int(input('数字 >'))
        if i == 0 or i == 1:
            print(f'{i}を入力したので、処理を終了します')
            break

def sixth():
    for i in range(10):
        i = int(input('数字いれて > '))
        if i == 0:
            print('0を入力したので、処理を終了します')
            break


if __name__ == '__main__':
    first()
    second()
    third()
    fourth()
    fifth()
    sixth()
