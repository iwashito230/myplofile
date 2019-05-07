#スキップ
'''
この演習は、
ハングマン演習シリーズのパート3の3です。

他の演習は次のとおりです。パート1とパート2。

Pythonの旅はどこからでも始めることができますが、
この課題を終えるには、第1 部と第2 部を終了するか、
解決策（第1 部と第2部）を使用する必要があります。

この演習では、Hangmanの構築を終了します。
ハングマンのゲームでは、
プレイヤーはゲームに負ける前に6回の誤った推測（頭、体、2本の足、2本の腕）を持っています。

パート1では、
ランダムな単語リストを読み込み、そこから単語を選びました。
第2回では、
文字を推測してその情報をユーザーに表示するためのロジックを作成しました。この課題では、それをすべてまとめて、推測を処理するためのロジックを追加する必要があります。

開始点として、
パート1と2から新しいファイルにコードをコピーします。
次の機能を追加してください。

・ユーザーに6回だけ推測させ、残りの推測数をユーザーに伝えます。
・ユーザーが推測した文字を追跡します。
ユーザーがすでに推測している文字を推測した場合は、
それらにペナルティを科さないでください - もう一度推測させてください。

オプションの追加：

・プレイヤーが勝ったり負けたりしたら、新しいゲームを始めましょう。
・ユーザー"You have 4 incorrect guesses left"に伝えるのではなく、
ハングマンのために絵のアートを表示します。
これはやりがいがあります - 最初に練習の他の部分をやってください！
あなたがあなたを助けるために関数を利用するならば、

あなたの解決策はずっときれいになるでしょう！
'''
import random


def pick_random_word():
    '''
    この関数はSOWPODSからランダムな単語を選択します
    This function picks a random word from the SOWPODS
    dictionary.
    '''
    #open the sowpods dictionary(sowpods辞書を開く)
    with open('sowpods.txt', 'r') as f:
        word = f.readlines()

        # generate a random index(ランダムインデックスを生成する)
        # -1 because len(words) is not valid index into the list 'words'
        #len(words）はリスト 'words'への有効なインデックスではないので-1)
        index = random.randint(0, len(word) - 1)

        #print out the word at that index
        word = word[index].strip()
        return word


def ask_user_for_next_letter():
    letter = input('Guess your letter: ')
    return letter.strip().upper()


def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append('_')
    return ''.join(output)


if __name__ == '__main__':
    WORD = pick_random_word()

    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0

    print('Welcome to Hangman!')
    while (len(letters_to_guess) > 0) and num_guesses < 6:
        guess = ask_user_for_next_letter()

        #check if we already guessed that(すでに推測しているかどうか確認してください)
        # letter
        if guess in correct_letters_guessed or \
                guess in incorrect_letters_guessed:
            # print out a message
            print('You already guessed that letter.(あなたはすでにその手紙を推測しました)')
            continue

        # if the guess was correct(推測が正しかった場合)
        if guess in letters_to_guess:
            # update the letters_to_guess(letters_to_guessを更新する)
            letters_to_guess.remove(guess)
            # update the correct letters_guessed(letters_guessedを更新する)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            # only update the number of guesses(推測数のみ更新する)
            # if you guesses incorrectly(あなたが間違って推測した場合)
            num_guesses += 1
        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print(f'You have {6 - num_guesses} guesses left.')

    # tell the user they have won or lost
    if num_guesses < 6:
        print(f'Congratulations! You correctly guessed the word {WORD}')
        print('おめでとうございます！あなたは正しく単語を推測しました')
    else:
        print(f'Sorry, you list! You word was {WORD}')
        print('すみません。あなたの言葉をリストします、あなたの言葉は')
