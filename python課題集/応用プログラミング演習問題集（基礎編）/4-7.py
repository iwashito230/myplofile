'''
文字で作った絵を2つ作りましょう．
そして，キーボードから入力した数が10 以上20 以下なら1つ目の絵を，
50以上60以下なら2つ目の絵を表示するプログラムを作りなさい．
'''

def main():
    emojibox = {'1': '(☝ ՞ਊ ՞)＝☞)՞ਊ ՞)', '2': '(⊙◞౪◟⊙)'}
    i = int(input('Please enter an integer: '))

    if i >= 10 and i <= 20:
        print(emojibox['1'])
    elif i >= 50 and i <= 60:
        print(emojibox['2'])
    else:
        pass

if __name__ == '__main__':
    main()
