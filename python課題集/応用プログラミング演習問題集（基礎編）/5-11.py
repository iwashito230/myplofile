'''
数当てゲームを作りたい．
１から100までのランダムな整数を用意し，
キーボードから入力した数がその数と同じならば
終了するプログラムを作成する．
'''
import random


def main():
    print('( ᐛ ) 数当てゲームを始めるよ └(՞ةڼ◔)」')
    print('=======================================')

    while True:
        num = random.randint(1, 10)
        i = int(input('作られた数字(1から100まで)を予想していれてね > '))
        if i == num:
            print('あったりーイェェ▂▅▇█▓▒░(‘ω’)░▒▓█▇▅▂ェェェイ')
            break
        else:
            print('ちがうよ！(´・д・｀)')
            if num >= i:
                print('もうちょっと大きい数字だお')
            elif num <= i:
                print('ちょっと小さい数字ですなー')
            continue


if __name__ == '__main__':
    main()
