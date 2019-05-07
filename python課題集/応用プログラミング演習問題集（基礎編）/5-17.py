'''
1から100までの素数を書き出すプログラムを作りなさい【難】

'''
import sympy


def main():
    primerange = sympy.primerange(1, 100)
    print(f'1から100までの素数は、{list(primerange)}です')


if __name__ == '__main__':
    main()
