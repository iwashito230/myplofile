# スキップ
'''
番号付きの順序付きリスト
（要素が最小から最大の順に並んでいるリスト）と
別の番号をとる関数を作成します。
この関数は与えられた数が
リストの中にあるかどうかを判断して適切なブール値を返します
（そしてそれから出力します）。

補足：

二分検索を使用します。

2文検索を用いての回答を写経。

'''

def find(ordered_list, element_to_find):
    start_index = 1
    end_index = len(ordered_list) - 1

    while True:
        middle_index = (end_index - start_index) / 2

        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False

        middle_element = ordered_list[middle_index]
        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index


if __name__ == '__main__':
    l = [2, 4, 6, 8, 10]
    print(find(l, 5))  # prints False
    print(find(l, 10))  # prints True
    print(find(l, -1))  # prints False
    print(find(l, 2))  # prints True
