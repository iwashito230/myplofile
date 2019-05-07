'''
1から9の間の乱数（1から9を含む）を生成します。
ユーザーに数字を推測してもらい、推測が低すぎる、
高すぎる、または正確かどうかを伝えます。
（ヒント：最初の演習からのユーザー入力レッスンを忘れずに使用してください）
'''
import random

def main():
    number = random.randint(1, 9)
    while True:
        input_number = int(input('1から9のどの数字かあててね > '))
        if input_number == number:
            print('正解～～～～～')
            break
        elif input_number <= number:
            print('ちょっと小さすぎます')
            continue
        elif input_number >= number:
            print('ちょっと大きすぎます')
            continue


if __name__ == '__main__':
    main()
