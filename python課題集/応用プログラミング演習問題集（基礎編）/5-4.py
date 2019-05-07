''' （while文）
（１）1から10までの整数を表示するプログラムを作りなさい．
（２）1から20までの整数を表示するように書き換えよ．
（３）-10から10までの整数を表示するように書き換えよ．
（４）2,4,6,8,10 を表示するように書き換えよ．
（ヒント：iを2つずつ大きくすると…）
（５）while i<=10: を while i<10: とするとどうなるか，試せ．
また，どうしてそうなるのか，考察せよ．
'''

def first():
    num = 1
    while num <= 10:
        print(num)
        num += 1

def second():
    num = 1
    while num <= 20:
        print(num)
        num += 1

def third():
    num = -10
    while num <= 10:
        print(num)
        num += 1

def fourth():
    i = 2
    while i <= 10:
        print(i)
        i += 2

def fifth():
    i = 2
    while i < 10:
        print(i)
        i += 2

if __name__ == '__main__':
    first()
    second()
    third()
    fourth()
    fifth()
