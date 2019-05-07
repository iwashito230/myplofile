#スキップ
'''
この演習は、ハングマン演習シリーズのパート2の3です。
他の演習は次のとおりです。パート1とパート3。

ハングマンを作り続けましょう。

ハングマンのゲームでは、プレイヤーが推測しなければならない
という手がかりとなる言葉がプログラムによって与えられます。

単語全体が推測されるまで、プレーヤーは一度に1文字ずつ推測します。
（実際のゲームでは、プレーヤーは負ける前に間違って6文字しか推測できません）。

プレイヤーが推測しなければならない単語が
「EVAPORATE」であるとしましょう。

この演習では、
プレイヤーに手紙を推測するように依頼し、
正しい推測された手がかりの単語に手紙を表示するロジックを作成します。

今のところ、彼らは単語全体を取得するまで、
プレイヤーは無限回を推測しましょう。

ボーナスとして、
プレイヤーが推測した文字を追跡し、
プレイヤーがその文字をもう一度推測しようとした場合は
別のメッセージを表示します。

すべての文字が正しく推測されたらゲームを停止することを忘れないでください！

ランダムに単語を選択したり、
プレイヤーが残っている推測の数を追跡したりすることについて心配しないでください

- 今後の課題でそれらを扱います。

対話の例は次のようになります。

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
そして、プレーヤーがその言葉を受け取るまで、それが続きます。
'''
if __name__ == '__main__':
    print('Welcome to hangman!!')
    word = 'EVAPORATE'
    guessed = '_' * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input('guess letter(手紙を推測): ')
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print('Already guessed!!(すでに推測されました)')
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = ''
        else:
            print(''.join(guessed))
            if letter is not '':
                lstGuessed.append(letter.upper())
                letter = input('guess letter(手紙を推測): ')

        if '_' not in guessed:
            print('You won!!（あなたの勝ち）')
            break
