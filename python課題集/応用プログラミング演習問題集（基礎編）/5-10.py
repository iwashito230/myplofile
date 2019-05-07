'''
1から100までのランダムな整数をxに代入し，
xが偶然50になるまで，その数値を
表示させ続けるプログラムを作りなさい．
（※最初の行にimport randomと宣言した上で，
x=random.randint(a,b)と書くことで，
xにaからbまでのランダムな整数を代入してくれる．）
'''
import random


def main():
    while True:
        num = random.randint(1, 100)
        if num == 50:
            print(num)
            print('50がでたので、終了')
            break
        else:
            print(num)
            continue


if __name__ == '__main__':
    main()
