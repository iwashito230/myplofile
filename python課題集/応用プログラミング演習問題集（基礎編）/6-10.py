'''
最初の行でimport randomと入力した上で、
x= random.randint(1,100)という命令は，xに0～99の適当な（ランダムな）数を代入するものです．
これを100回行って，xに30以下の数が何回代入されたかを表示するプログラムを作りなさい．
'''
import random


def main():
    count = 0
    for x in range(100):
        x = random.randint(1, 100)
        if x <= 30:
            count = count + 1
    print(f'30以下の数字は{count}回代入されました')


if __name__ == '__main__':
    main()
