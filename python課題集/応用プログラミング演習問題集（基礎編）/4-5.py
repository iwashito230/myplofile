'''
キーボードから数値をxに入力し，
ifを使って，xが偶数ならGuusuu，奇数ならKisuuと表示させるプログラムを作りなさい．
xが偶数なら，xを2で割った余りが0となり，奇数であれば1になるので，
xを2で割った余りを調べれば良いです．余りを計算するには%を使います．
'''

def main():
    x = int(input('Please enter an integer: x = '))

    if x % 2 == 0:
        print('Guusuu')
    else:
        print('Kisuu')

if __name__ == '__main__':
    main()
