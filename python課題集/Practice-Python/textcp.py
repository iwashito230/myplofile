from pathlib import Path
import requests

from bs4 import BeautifulSoup

def main():
    resp = requests.get(input('URL > '))
    soup = BeautifulSoup(resp.text, 'html.parser')

    filename = input('保存ファイル名？ > ')
    path = f'{Path.cwd()}/{filename}'
    if not Path(filename).exists():
        Path(filename).touch()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            print('内容を保存')
    else:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(soup))
            print('追記保存')


if __name__ == '__main__':
    main()
