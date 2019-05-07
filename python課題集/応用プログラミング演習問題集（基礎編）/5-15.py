'''
3×3×3のかけ算の表を表示するプログラムを作りなさい．
1×1×1，1×1×2，1×1×3，1×2×1，．．．の順で表示するようにしなさい．

'''

def main():
    for x in range(1, 4):
        for y in range(1, 4):
            for z in range(1, 4):
                print(f'{x} × {y} × {z} = {x * y * z}', end='\n')
            print('\n')


if __name__ == '__main__':
    main()
