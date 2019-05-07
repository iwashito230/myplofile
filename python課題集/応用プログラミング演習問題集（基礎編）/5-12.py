'''
２つの整数aとbをキーボードから入力させ，
a以上b以下の整数をすべて表示させるプログラムを作れ
（１）for文を使って作れ（whileは使わない）
（２）while文を使って作れ（forは使わない)

'''

def first():
    a = int(input('a = '))
    b = int(input('b = '))
    lists = range(a, (b + 1))

    for li in lists:
        print(li)


def second():
    a = int(input('a = '))
    b = int(input('b = '))
    while a <= b:
        print(a)
        a += 1


if __name__ == '__main__':
    first()
    second()
