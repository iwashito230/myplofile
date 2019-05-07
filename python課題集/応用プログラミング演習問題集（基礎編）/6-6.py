'''
足し算だけの電卓を作りなさい．
数を入力し，今まで入力した数の合計を表示する，
という作業を繰り返すプログラムです．
さらに，0 を入力したときは終了するようにしなさい．
例えば，10,20,63,0 と入力すると，このようになります．「10 10 20 30 63 93 0」
'''
def main():
    while True:
        numbers = list(map(int, input('合計したい数字をいれてください > ').split()))
        if 0 in numbers:
            print('0が入力されました、計算を終了します')
            break
        else:
            print(f'合計は、{sum(numbers)}')
            break


if __name__ == '__main__':
    main()
