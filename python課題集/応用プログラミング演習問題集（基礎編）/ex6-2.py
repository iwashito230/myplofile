'''
10個の数を入力して，その中で最大のものを表示する，というプログラムを作りましょう．
（サンプルコード）
m = -9999
for i in range(10) :
    j = input("Please enter an integer:")
    if m < j :
        m=j
print m

'''

def main():
    m = -9999
    for i in range(10):
        j = int(input('整数入れなはれや > '))
        if m < j:
            m = j
    print(f'この中での最大整数は、{m}')


if __name__ == '__main__':
    main()
