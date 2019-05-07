'''
ifの入れ子を使ったプログラムを作りましょう．
入力した数が正の場合はpositiveと表示して,
さらに100以上の場合は100ijou，100未満の場合は100mimanと表示しましょう．
また，入力した数が正でない場合，0の場合はzero，負の場合はnegativeと表示しましょう．
'''

def main():
    x = int(input("Please enter an integer:"))
    if x > 0:
        print('positive')
        if x >= 100:
            print('100ijou')
        else:
            print('100miman')
    elif x == 0:
        print('zero')
    else:
        print('negative')

if __name__ == '__main__':
    main()
