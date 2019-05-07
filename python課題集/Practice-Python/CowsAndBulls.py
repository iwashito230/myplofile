# スキップ
'''
ユーザーと「牛と雄牛」のゲームをプレイするプログラムを作成します。
ゲームはこのように動作します：

4桁の数字をランダムに生成します。
ユーザーに4桁の数字を推測するように依頼します。
ユーザーが正しい場所で正しく推測した数字ごとに、「牛」があります。
ユーザーが間違った場所で正しく推測した数字はすべて「雄牛」です。
ユーザーが推測するたびに、「牛」と「雄牛」の数を伝えます。
ユーザーが正しい番号を推測すると、ゲームは終了です。
ユーザーがゲーム全体を通して行った推測の数を追跡し、最後にユーザーに伝えます。

コンピュータによって生成された数が1038だとします。インタラクションの例は次のようになります。

  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
ユーザーが数字を推測するまで。
**英単語不明だったところのmemo
guess: 推測

'''

import random


def compare_numbers(number, user_guess):
    cowbull = [0, 0] #cows, then bulls

    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1] += 1
        else:
            cowbull[0] += 1
    return cowbull


if __name__ == '__main__':
    playing = True #gotta play the game(ゲームをプレイしなければならない)
    number = str(random.randint(0, 9999)) #random 4 digit number(ランダムな4桁の数字)
    guesses = 0

    #牛と雄牛のゲームをしましょう
    print("Let's play a game of Cowbull!") #explanation(説明)
    #私は数を生成します。そしてあなたは数を一度に一桁ずつ推測しなければなりません。
    print('I will generate a number, and you have to guess the numbers one digit at a time.')
    #間違った場所にある全ての番号に対して、あなたは牛を飼います。正しい場所にいる一人ひとりのために、あなたは雄牛を得ます。
    print('For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.')
    #あなたは４雄牛を得るとゲームは終了します
    print('The game ends when you get 4 bulls!')
    #終了するプロンプトがでたらexitと入力します

    while playing:
        #あなたの最善の推測をください
        user_guess = input('Give me your best guess!')
        if user_guess == 'exit':
            break
        cowbullcount = compare_numbers(number, user_guess)
        guesses += 1

        #あなたは○○牛と○○雄牛をかっています
        print(f'You hove {str(cowbullcount[0])} cows, and {str(cowbullcount[1])} bulls.')

        if cowbullcount[1] == 4:
            playing = False
            #あなたはあと○○あわせればゲームに勝ちます
            print(f'You win the game after {str(guesses)}! The number was {str(number)}')
            break #remdudant exit(残り数)
        else:
            #あなたの推測は全く正しくありません、もう一度やりなおしてください
            print("Your guess isn't quite right, try again.")
