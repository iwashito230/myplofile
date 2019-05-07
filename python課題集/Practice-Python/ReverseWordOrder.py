'''
複数の単語を含む長い文字列をユーザーに要求するプログラムを（関数を使用して）作成します。
逆順の単語を除いて、同じ文字列をユーザーに出力します。たとえば、文字列を入力したとします。

My name is Michele
それから私は文字列を見るでしょう：

  Michele is name My
私に戻って見せて。
'''

def main():
    user_input = list(map(str, input('すきな文章を単語ごとにスペースをいれながら入力してください > ').split()))
    reverse = user_input[::-1]
    print(''.join(reverse))


if __name__ == '__main__':
    main()
