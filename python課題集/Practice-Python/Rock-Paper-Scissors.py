'''
二人用のRock-Paper-Scissorsゲームを作りましょう。
（ヒント：プレイヤーのプレーを要求し（使用しinput）、
それらを比較し、勝者にお祝いのメッセージを印刷し、
そしてプレイヤーが新しいゲームを開始したいかどうかを尋ねます）

規則を覚えておいてください：

ロックビートはさみ
はさみが紙を打ちます
紙が岩を打つ
'''

def main():
    while True:
        name1 = input('名前を入力してください > ')
        name2 = input('次の人の名前を入力してください > ')
        player1 = input(f'{name1}さん Rock、Paper、Scissorsどれかを選んでください > ')
        player2 = input(f'{name2}さん Rock、Paper、Scissorsどれかを選んでください > ')
        choice = [player1, player2]
        if choice == ['Rock', 'Paper']:
            print(f'{name2}の勝ちです、おめでとう')
            break
        elif choice == ['Rock', 'Scissors']:
            print(f'{name1}の勝ちです、おめでとう')
            break
        elif choice == ['Paper', 'Rock']:
            print('{name1}の勝ちです、おめでとう')
            break
        elif choice == ['Scissors', 'Rock']:
            print('{name2}の勝ちです、おめでとう')
            break
        elif player1 == player2:
            print('引き分け')
            break
        else:
            print('もう一度選択してください')
            continue


def continue_anther():
    while True:
        anther = input('ゲームをつづけますか？ y or n > ')
        if anther == 'y':
            main()
        elif anther == 'n':
            break
        else:
            continue


if __name__ == '__main__':
    main()
    continue_anther()
