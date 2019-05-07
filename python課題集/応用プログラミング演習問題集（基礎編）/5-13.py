'''
２つの整数a,bをキーボードから入力し，
縦がa文字，横がb文字の*で出来た四角を描くプログラムを作りなさい．
たとえば，a=2,b=5なら，
*****
*****
と表示される．
（１）forを１回だけ使用して作れ
（２）２重のforループを使用して作れ【やや難】

'''


def first():
    a = int(input('縦の大きさ > '))
    b = int(input('横の大きさ > '))
    for draw_a_square in range(a):
        draw_a_square = ''.join('*' * b)
        print(draw_a_square)

def second():
    a = int(input('縦の大きさ > '))
    b = int(input('横の大きさ > '))
    for width in range(a):
        for height in range(b):
            print('*', end='')
        print(end='\n')


if __name__ == '__main__':
    first()
    second()
