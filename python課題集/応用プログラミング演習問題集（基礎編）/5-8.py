'''
 ##########        1個の空白と10個の#を表示
  ########         2個の空白と8個の#を表示
   ######          3個の空白と6個の#を表示
    ####           4個の空白と4個の#を表示
     ##            5個の空白と2個の#を表示
上のような#で作った三角形を表示するプログラムを作成せよ．【やや難】
'''

def main():
    top = 5
    for index in range(top):
        for n in range(index):
            print(' ', end='')
        for n in range((top-index)* 2-1):
            print('*', end='')
        print()


if __name__ == '__main__':
    main()
