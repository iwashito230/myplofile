'''
ユーザーに文字列を要求し、この文字列が回文かどうかを表示します。
（回文とは、前後に同じ文字を読む文字列です。）
'''

def main():
    str_input = input('文字列をいれてください > ')
    if str_input == str_input[::-1]:
        print('回文ですね')
    else:
        print('普通の文字列ですね')


if __name__ == '__main__':
    main()
