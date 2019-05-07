'''
「入力した10個の数の中に5があるかどうか」を調べるプログラムを作りましょう．
以下のプログラムでは，fをフラグにしています．
（サンプルコード）
f = 0
for i in range(10) :
    j = input("Please enter an integer:")
    if j == 5 :
        f = 1
if f == 1 :
    print '5 ga atta'

'''

def main():
    f = 0
    for i in range(10):
        j = int(input('整数をいれてね > '))
        if j == 5:
            f = 1
    if f == 1:
            print('5がありました')

if __name__ == '__main__':
    main()
