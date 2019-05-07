#スキップ
'''
このエクササイズは、チックタックトーのエクササイズシリーズのパート４の４です。
その他の演習は、パート1、パート2、およびパート3です。

これまでの3つの演習では、
Tic Tac ToeゲームをPythonで作成するために必要ないくつかのコンポーネントを作成しました。

1.チックタックトーゲームボードを描く
2.ゲームボードに勝者がいるかどうかの確認
3.ユーザー入力からプレーヤーの移動を処理する
次のステップは、
これら3つのコンポーネントすべてをまとめて2人用のチックタックトーゲームを作ることです。

この練習でのあなたの挑戦は
あなたが友人と遊ぶことができる2人用のゲームを作るために
同じプログラムの中でそれらの以前の練習からの機能をすべて一緒に使うことです。

この練習を完了するときにあなたがしなければならないであろう多くの選択があります、
従ってあなたはあなたがそれを望んでいる限り遠くにまたは少しでも行くことができます。

ここで留意すべきことがいくつかあります。

あなたは誰が勝ったかを追跡し続けるべきです 
- 勝者がいるならば、スクリーンにお祝いのメッセージを示してください。

それ以上移動がない場合は、次のプレイヤーの移動を要求しないでください。
ボーナスとして、あなたは彼らが再びプレイしたいかどうかプレイヤーに尋ねることができます。

*英単語めも
convert: 変換する
coordinate: 座標
available: 利用可能
'''
def draw_line(width, edge, filling):
    print(filling.join([edge] * (width +1)))


def display_winner(player):
    if player == 0:
        print('Tie')
    else:
        print(f'Player {str(player)} + wins!')


def check_row_winner(row):
    '''
    Return the player number that wins for that row.
    その行に買ったプレイヤー番号を返します
    if there is no winner, return 0.
    勝者がいなければ0を返す。
    '''
    if row[0] == row[1] and row[1] == row[2]:
        return row[0]
    return 0


def get_col(game, col_number):
    return [game[x][col_number] for x in range(3)]


def get_row(game, row_number):
    return game[row_number]

def check_winner(game):
    game_slices = []
    for index in range(3):
        game_slices.append(get_row(game, index))
        game_slices.append(get_col(game, index))
    #check diagonals(対角線をチェック)

    down_diagonal = [game[x][x] for x in range(3)]
    up_diagonal = [game[0][2], game[1][1], game[2][0]]
    game_slices.append(down_diagonal)
    game_slices.append(up_diagonal)

    for game_slice in game_slice:
        winner = check_row_winner(game_slice)
        if winner != 0:
            return winner

    return winner


def start_game():
    return [[0, 0, 0] for x in range(3)]


def display_game(game):
    d = {2: 'O', 1: 'X', 0: '_'}
    draw_line(3, ' ', '_')
    for row_num in range(3):
        new_row = []
        for col_num in range(3):
            new_row.append(d[game][row_num][col_num])
            print(f'| {|.join(new_row)} |')


def add_piece(game, player, row, colunm):
    '''
    game: game start
    player: player number
    row: 0 index row
    cloumn: 0 index column
    '''
    game[row][column] = player
    return game


def check_space_empty(game, row, column):
    return game[row][column] == 0


def convert_input_to_coordinate(user_input):
    return user_input - 1


def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1


def moves_exist(game):
    for row_num in range(3):
        for col_num in range(3):
            if game[row_num][col_num] == 0:
                return True
    return False


if __name__ == '__main__':
    game = start_game()
    display_game(game)
    player = 1
    winner = 0  # the winner is not yet defined(勝者はまだ定義されていません)

   # go on forever(永遠に続行)
   while winner == 0 and moves_exist(game):
       print(f'Currently player: {str(player)}')
       available = False
       while not available:
           row = conert_input_to_coordinate(int(input('Which row? (start with 1)[どの行？1から始める？] ')))
           column = covert_input_to_coordinate(int(input('Whilch column? (start with 1)[どの列？1から始める？] ')))
           available = check_space_empty(game, row, column)
        game = add_piece(game, player, row, column)
        display_game(game)
        player = switch_player(player)
        winner = check_winner(game)
    display_winner(winner)
