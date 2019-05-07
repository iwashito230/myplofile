''' 以下のプログラムは，xとyの値を3回表示するのですが，それぞれ，何と何が表示されると思いますか？ 
    プログラムがどのように動いて，変数には何が代入されるかを考えた上で，① 10,10  ② 10,20  ③ 20,20の中から選んで下さい
   （サンプルコード）
    x = 10
    y = 10
    print x,y
    A. 1

    x = y+10
    y = 20
    print x,y

    A. 3
    
    x = x-10
    y = y-x
    print x,y
    
    A. 1
'''

def main():
    x = 10
    y = 10
    print(x, y)

    x = y+10
    y = 20
    print(x, y)

    x = x-10
    y = y-x
    print (x, y)

if __name__ == '__main__':
    main()
