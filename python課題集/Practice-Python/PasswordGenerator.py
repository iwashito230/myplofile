'''
Pythonでパスワードジェネレータを書いてください。
どのようにパスワードを生成するかについて創造的になりましょう 
- 強力なパスワードには、
小文字、大文字、数字、および記号が混在しています。
パスワードはランダムである必要があり、
ユーザーが新しいパスワードを要求するたびに
新しいパスワードを生成します。
ランタイムコードをメインメソッドに含めます。

'''
import string, random


def main():
    pw = ''.join([random.choice(string.printable) for i in range(8)])
    print(pw)


if __name__ == '__main__':
    main()
