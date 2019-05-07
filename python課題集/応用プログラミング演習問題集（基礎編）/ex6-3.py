'''
「入力した10個の数の中に10以上のものはいくつあるか」というプログラムを作りましょう．
（サンプルコード）
c = 0
for i in range(10) :
    j = input("Please enter an integer:")
    if j >=10 :
        c += 1
print c
'''

def main():
    c = 0
    for i in range(10):
        j = int(input('整数をいれてね > '))
        if j >= 10:
            c += 1
    print(f'10以上の数は、{c}つありました')

if __name__ == '__main__':
    main()
