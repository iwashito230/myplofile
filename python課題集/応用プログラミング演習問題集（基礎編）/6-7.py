'''
入力した10個の数の中に1と0，
どちらが多いかを判定するプログラムを作りなさい．

'''


def main():
    while True:
        numbers = list(map(int, input('10個 0か1を入力してください > ').split()))
        if len(numbers) == 3:
            one_list = [o for o in numbers if o == 1]
            zero_list = [z for z in numbers if z == 0]
            other_list = [oth for oth in numbers if oth != 0 and oth != 1]
            if len(other_list) > 0:
                print('0か1でいれてください')
                continue
            else:
                if len(one_list) > len(zero_list):
                    print(f'1のが{len(one_list)}個多いです')
                    break
                elif len(zero_list) > len(one_list):
                    print(f'0のが{len(zero_list)}個多いです')
                    break
                else:
                    print('同じ数でした')
        else:
            print('10個いれられていません')
            continue


if __name__ == '__main__':
    main()
