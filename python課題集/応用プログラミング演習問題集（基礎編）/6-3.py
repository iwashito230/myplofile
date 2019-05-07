'''
キーボードから１０個の数字を入力し，
(1)負の数がいくつ入力されたかを表示するプログラムを作りなさい．
(2)偶数がいくつ入力されたかを表示するプログラムを作りなさい．
'''


def first():
    while True:
        receive = list(map(float, input('10個数字を入力してください > ').split()))
        if len(receive) == 10:
            minus_list = [minus for minus in receive if minus <= 0]
            print(f'負の数の数は、全部で{len(minus_list)}個です')
            break
        else:
            print('もう一度いれてください')
            continue

def second():
    while True:
        receive = list(map(float, input('10個の数字を入力してください > ').split()))
        if len(receive) == 10:
            even_list = [even for even in receive if even % 2 == 0]
            print(f'偶数は、全部で{len(even_list)}個入れられました')
            break
        else:
            print('もう一度いれてください')
            continue

if __name__ == '__main__':
    first()
    second()
