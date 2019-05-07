'''
（1）入力した数が0ならzeroと表示するプログラムを作りましょう．
（2）入力した数が100以上ならOKと表示するプログラムを作りましょう．
（3）入力した数が0以上ならpositive，そうでなければnegativeと表示するプログラムを作りましょう．
（4）入力した2つの数が等しいならequalと表示するプログラムを作りましょう．

'''

def first():
    i = int(input('Please enter an integer: '))
    if i == 0:
        print('zero')

def second():
    i = int(input('Please enter an integer: '))
    if i > 100:
        print('OK')

def third():
    i = int(input('Please enter an integer: '))
    if i > 0:
        print('positive')
    else:
        print('negative')

def forth():
    x = int(input('Please enter an integer: x = '))
    y = int(input('Please enter an integer: y = '))

    if x == y:
        print('equal')


if __name__ == '__main__':
    first()
    second()
    third()
    forth()
