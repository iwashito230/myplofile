''' 整数と小数を使ったプログラムを実行してみましょう．
    このプログラムは，小数である9.99と整数である50をそれぞれ10倍して表示します．
'''

def main():
    data = [9.99, 50]
    multiplied = [d*10 for d in data]
    for m in multiplied:
        print(m)

if __name__ == "__main__":
    main()

