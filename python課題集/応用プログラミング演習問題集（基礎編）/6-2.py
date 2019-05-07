'''
(1)「入力した10個の数の最小」を表示するプログラムを作りなさい．

(2)「10以下の数の中での最大」を表示するようなプログラムを作りなさい．
ただし，10以下の数は必ず1つは入力される，とみなして良いとします．
'''

def first():
    num = [int(input('すきな整数を10個入れてください > ')) for i in range(10)] 
    print(f'入力した10個の数の最小は、 {min(num)}です')


def second():
    num = list(map(int, input('すきな整数を10個入れてください > ').split()))
    under_10 =[u for u in num if u <= 10]
    print(f'10以下の数の中での最大の数は、{max(under_10)}です')

if __name__ == '__main__':
    first()
    second()
