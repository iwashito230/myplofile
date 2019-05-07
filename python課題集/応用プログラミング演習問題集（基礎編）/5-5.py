'''
（for文）（▲参考：例題５－７）
（１）問題５－４の各問をforループを用いて書き換えよ
（２）10から1までの整数を大きい順で（10,9,8,… ）表示せよ．
（３）1から100までの偶数を表示せよ．
'''

class first():
    def fir_1():
        print('1から10までの整数を表示するプログラムを作りなさい')
        num = [num+1 for num in range(10)]

        for n in num:
            print(n)

    def fir_2():
        print('1から20までの整数を表示するように書き換えよ．')
        num = [num+1 for num in range(20)]

        for n in num:
            print(n)

    def fir_3():
        print('-10から10までの整数を表示するように書き換えよ．')
        num = [num for num in range(-10, 10)]

        for n in num:
            print(n)

    def fir_4():
        print('2,4,6,8,10 を表示するように書き換えよ．')
        num = [num for num in range(2, 11, 2)]

        for n in num:
            print(n)

    def fir_5():
        print('i<=10: を i<10: とするとどうなるか，試せ．また，どうしてそうなるのか，考察せよ．')
        num = [num for num in range(2, 10, 2)]

        for n in num:
            print(n)

class second():
    def sec():
        num = [num+1 for num in range(10)]

        for n in reversed(num):
            print(n)

class third():
    def thi():
        num = [num for num in range(2, 101) if num % 2 == 0]

        for n in num:
            print(n)


if __name__ == '__main__':
    first.fir_1()
    first.fir_2()
    first.fir_3()
    first.fir_4()
    first.fir_5()
    second.sec()
    third.thi()
