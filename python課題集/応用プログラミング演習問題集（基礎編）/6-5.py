'''
数を10個入力してその合計を表示するプログラムを作りなさい．

'''

def main():
    while True:
        num = list(map(int,input('すきな数字を10個入れて下さい > ').split()))
        if len(num) == 10:
            print(sum(num))
            break
        else:
            print('10個数字が入力されていません！')
            continue


if __name__ == '__main__':
    main()
