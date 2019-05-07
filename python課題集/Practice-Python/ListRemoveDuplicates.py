'''
リストを受け取り、
最初のリストのすべての要素から
すべての重複を除いた新しいリストを返すプログラム（関数！）を作成します。

補足：

これを行うには2つの異なる関数を書きます。
1つはループを使用してリストを作成するもの、もう1つは集合を使用するものです。
戻ってセット5を使って実習5を行い、それに対する解決策を別の関数で書きます。
'''

def main():
    strlist = list(map(str, (input('すきな言葉を幾つかいれてください > ')).split()))
    while True:
        print(strlist)
        continue_anther = input('listに言葉を追加しますか? y or n > ')

        if continue_anther == 'y':
            addlist = list(map(str, input('追加したい言葉をいれてください > ').split()))
            g = strlist + addlist
            strlist = list(set(g))
            continue
        elif continue_anther == 'ｙ':
            print('半角でいれてください')
            continue
        else:
            print('言葉を追加するのを中止します')
            break


if __name__ == '__main__':
    main()
