'''
入力した数が素数かどうかを判定するプログラムを作りなさい．
(ヒント：ある数xが素数ならば，2以上x未満の数で，xを割り切るものがありません．
そこで，2からx-1までのループを作り，
それぞれでxを割った余りが0になるかどうか判定し，
0になったらフラグ変数にそのことを記録しましょう)

'''
import sympy


def main():
    check_input = int(input('すきな数をいれてください > '))
    if sympy.isprime(check_input):
        print(f'{check_input}は、素数です')
    else:
        print(f'{check_input}は、素数じゃないです')


if __name__ == '__main__':
    main()
