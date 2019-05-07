'''
例題４－３のサンプルコードを用いて，
（1）入力した数が10か10より大きいか10未満かを判定するプログラムを作りましょう．
（2）入力した数が1なら1，2なら2，それ以外ならetcと表示させましょう．
（3）最初のifの条件式を(x<0)とすると，実行結果は元のプログラムと変わってしまいます．
     そこで，この条件式以外の部分を修正して，元のプログラムと同じ実行結果を出すプログラムに修正しましょう．
'''

def first():
    x = int(input("Please enter an integer:"))
    if x >= 10:
        print('10ijou')
    elif x < 10:
        print('10miman')

def second():
    x = int(input("Please enter an integer:"))
    if x == 1:
        print(x)
    elif x == 2:
        print(x)
    else:
        print('etc')

def third():
    x = int(input("Please enter an integer:"))
    if x <= 0 or x < 10:
        print('10miman')
    elif x >= 10:
        print('10ijou')


if __name__ == '__main__':
    #first()
    #second()
    third()
