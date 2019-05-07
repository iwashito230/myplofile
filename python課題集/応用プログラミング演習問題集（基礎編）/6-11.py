'''
10個の数を入力し，
「前回と同じ数を入力した回数」を勘定するプログラムを作りなさい．
例えば，2,2,4,4,4と入力すると，3回と表示します．
'''
import collections


def main():
    while True:
        input_numbers = list(map(int, input('整数を10個入れてください > ').split()))
        if len(input_numbers) == 10:
            count = collections.Counter(input_numbers)
            most = count.most_common()[0][1]
            print(f'同じ数字は最大{most}回入力されました')
            break
        else:
            print('10個数字が入力されていません')
            continue


if __name__ == '__main__':
    main()
