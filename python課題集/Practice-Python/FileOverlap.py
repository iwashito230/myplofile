#スキップ
'''
2つの.txtファイルに番号のリストが含まれていると仮定して、
重複している番号を見つけます。
一方の.txtファイルには1000未満のすべての素数のリストがあり、
もう一方の.txtファイルには最大1000までの幸せな番号のリストがあります。

（忘れた場合、素数は他の数で割り切れない数です。
そうです、幸せな数は数学では本当のことです 
- あなたはそれをウィキペディアで調べることができます。
以下に説明します。）

'''

def filetolistofints(filename):
    list_to_return = []
    with open(filename) as f:
        line = readline()
        while line:
            line_to_return.append(int(line))
            line = f.readline()
    return line_to_return

primeslist = filetolistofints('primenumbers.txt')
happineslist = filetoofints('happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)
