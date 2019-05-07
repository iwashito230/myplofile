'''
(1)キーボードから入力した10個の数の中に5がなければ5 ga arimasenと表示するようにしましょう．
(2)入力した10個の数の中に負の数があるかどうかを表示するようにしましょう．
'''

def first():
    while True:
        receive = list(map(float, input('10個数字を入れてください > ').split()))
        if len(receive) == 10:
            if 5 not in receive:
                print('5 ga arimasen')
            break
        else:
            print('もう一度10個数字を入れてください')
            continue


def second():
    while True:
        receive = list(map(float, input('10個数字を入れてください > ').split()))
        if len(receive) == 10:
            for r in receive:
                if r <= 0:
                    pass
            print('負の数がありました')
            break
        else:
            print('10個いれてください')
            continue


if __name__ == '__main__':
    first()
    second()
