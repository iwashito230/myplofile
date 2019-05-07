#スキップ
'''
で前の演習、我々は数を「知っている」と、それを推測するために、ユーザが要求するプログラムを書いています。

今回は、正反対のことを行います。
あなたは、あなたの頭の中に0と100の間の数を持っているでしょう。
プログラムは数を推測します、

そしてあなた、ユーザは、それが高すぎるか、低すぎるか、それともあなたの番号かを言います。

この交換の終わりに、あなたのプログラムはあなたの番号を取得するのに要した推測数を出力するべきです。

このプログラムの作家として、
あなたはあなたのプログラムが戦略的に推測する方法を選択しなければならないでしょう。

素朴な戦略は、単純に推測を1から開始し、数字に達するまで続けていくことです（2、3、4など）。

しかし、これは最適な推測戦略ではありません。

別の方法としては、50（範囲の中央）を推測してから、必要に応じて1ずつ増減します。

プログラムを作成したら、最適な戦略を見つけようとしてください。

（私たちはその解決策と共に来週最適なものについて話すでしょう。）

'''
def guess():
    i = 0
    # i は、可能な推測範囲内での最低の数値です
    # i is the lowest number in range of possible guess
    j = 100
    #jは、可能なす即範囲の最大の数値です
    #j is the heigest number in range of possible guesses
    m = 50
    # mは、可能な推測の中間の地点の数
    # m is the middle number in range og possible guesses
    counter = 1
    # counter は 推測した数です
    # counter is the number of guesses take.
    print('Please guess a number')
    # 0は1が、それはあなたの推測だ意味し、2はそれがあまりにも高いです意味、それは低すぎる
    str_m = str(m)
    condition = input(f"Is your guess {str_m} ? (0 means it's too low, 1 means it's your guess and 2 means it's too high)")
    while condition != 1:
        counter += 1
        if condition == 0:
            i = m + 1
        elif condition == 2:
            j = m - 1
        m = (i + j) / 2
        #0は1が、それはあなたの推測だ意味し、2はそれがあまりにも高いです意味、それは低すぎるのです意味
        condition = input(f"Is your guess {str_m} ? (0 means it's too low, 1 means it's your guess ans 2 means it's too high)")
    print(f'It took, {counter}, times to guess your number')
guess()
