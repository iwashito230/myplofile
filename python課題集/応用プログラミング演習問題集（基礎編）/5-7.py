'''
（１）forの2重ループを使って，九九の表を書くプログラムを作成せよ．
ただし，表の罫線を書くのは大変なので，中身の数字だけを書く．
（２）9×9 の足し算の答えを表にせよ．
（３）12×12 の掛け算の答えを表にせよ．

'''

def first():
    for x in range(1, 10):
        for y in range(1, 10):
            print(x * y, " ", end="")
        print('\n')

def second():
    for x in range(1, 10):
        for y in range(1, 10):
            print(x + y, " " , end="")
        print('\n')

def third():
    for x in range(1, 13):
        for y in range(1, 13):
            print(x * y, " ", end="")
        print('\n')


if __name__ == '__main__':
    first()
    second()
    third()
