#サンプル
'''
.txt多数の名前のリストを含むファイルがあるとします。
ファイル内に各名前がいくつあるかを数えて、結果を画面に出力します。
.txtあなたがそれを使いたいならば、私はあなたのためのファイルを持っています！

追加：

.txt上のファイルを使うのではなく（あるいは挑戦したいのであれば）、
この.txtファイルを使って、各画像の各「カテゴリ」の数を数えます。
このテキストファイルは、
実際にはSUNデータベースのシーン認識データベースに対応するファイルのリストであり、
画像のファイルディレクトリ階層をリストしています。
ファイルの最初の1行または2行を見ると、
どの部分がシーンカテゴリを表しているかが明らかになります。
これを行うには、Python 3での文字列解析について少し覚えておく必要があります。
この記事で少し話しました。
'''
counter_dict = {}
with open('Training_01.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()

print(counter_dict)
