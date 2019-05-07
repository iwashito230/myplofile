'''
キーボードから入力した数が10以上20以下であればOKと表示するプログラムを作りなさい．
'''

def main():
    i = int(input('Please enter an integer: '))
    if i >= 10 and i <= 20:
        print('OK')

if __name__ == '__main__':
    main()
