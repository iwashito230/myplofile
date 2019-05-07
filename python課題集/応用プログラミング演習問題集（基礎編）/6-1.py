'''
(1)前回入力した数より倍以上大きな数を入力したら終了するようなプログラムを作りなさい．
(2)前回入力した負の数と同じ数を入力したら終了するようにしましょう（1,-1,4,-4,5 と入力した時点では，前回入力した負の数は-4です）．
   （ヒント：xが負のときだけ，yにxを代入しましょう．）
(3)2回前に入力した数と同じ数を入力したら終了するようにしましょう．

'''

def first():
    while True:
        question = int(input('好きな数字をいれてください > '))
        question2 = int(input('好きな数字をいれてください > '))

        if question2 >= question * 2:
            print('先ほどの数字より倍以上大きくなった！ので終了')
            break


def second():
    while True:
        x = int(input('すきなせいすうを入れてください > '))
        y = int(input('すきなせいすうを入れてください > '))
        if x == -1 * y:
            print('負と同じ数をいれたので、処理を終了')
            break

def thired():
    while True:
        a = int(input('すきなせいすうを入れてください > '))
        b = int(input('すきなせいすうを入れてください > '))
        c = int(input('すきなせいすうを入れてください > '))
        if a == c:
            print('2回前のものと同じ値なので終了')


if __name__ == '__main__':
    first()
    second()
    thired()
