import os


print(list(os.scandir()))

with open('cui') as file:
    print(file.read())
import os

MENU = ' \n' \
       '1. Просмотр каталога \n' \
        '2. На уровень вверх \n' \
        '3. На уровень вниз \n' \
        '4. Количество файлов и каталогов \n' \
        '5. Размер текущего каталога (в байтах) \n' \
        '6. Поиск файла \n' \
        '7. Выход из программы \n'

QUIT = '7'


def acceptCommand():
    COMMANDS = [str(x) for x in range(1, 8)]

    command = input('Выберите пункт меню:')

    if command in COMMANDS:
        return command
    return None


def runCommand(command):
    pass


def moveUp():
    pass


def moveDown(currentDir):
    pass


def countFiles(path):
    pass


def countBytes(path):
    pass


def findFiles(target, path):
    pass


def main(): 
    while True: 
        print(os.getcwd())
        print(MENU)

        command = acceptCommand()
        runCommand(command)

        if command == QUIT: 
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()
