import os

MENU = ' \n' \
       '1. Просмотр каталога \n' \
        '2. На уровень вверх \n' \
        '3. На уровень вниз \n' \
        '4. Количество файлов и каталогов \n' \
        '5. Размер текущего каталога (в байтах) \n' \
        '6. Поиск файла \n' \
        '7. Выход из программы \n'

VIEW = '1'
UP = '2'
DOWN = '3'
NUM = '4'
SIZE = '5'
FIND = '6'
QUIT = '7'


def acceptCommand():
    """
    The function will check if the function number is valid.

    :return: If the number is correct, then the team number. If the number is incorrect, then NoneType.
    """

    COMMANDS = [str(x) for x in range(1, 8)]

    command = input('Выберите пункт меню: ')

    if command in COMMANDS:
        return command

    return None


def runCommand(command):
    pass


def moveUp():
    os.chdir('..')


def moveDown(currentDir):
    subDir = input('Введите имя подкаталога: ')
    elementPath = os.path.join(currentDir, subDir)

    if os.path.isdir(elementPath):
        os.chdir(subDir)

    else:
        print('Имя подкаталога указано неверно!')


def countFiles(path):
    """
    The function counts the number of files in the directory

    :param path: Path to the directory to search in
    :return: Number of files
    """

    count = 0
    elements = os.listdir(path)
    for element in elements:
        elementPath = os.path.join(path, element)
        if os.path.isfile(elementPath):
            count += 1
        else:
            count += countFiles(elementPath)
    return count


def countBytes(path):
    """
    The function calculates the total volume of files in a directory in Bytes

    :param path: Path to the directory to search in
    :return: the total volume of files in a directory in Bytes
    """
        
    amnt_Bytes = 0
    elements = os.listdir(path)
    for element in elements:
        elementPath = os.path.join(path, element)
        if os.path.isfile(elementPath):
            amnt_Bytes += os.path.getsize(elementPath)
        else:
            amnt_Bytes += countBytes(elementPath)
    
    return amnt_Bytes


def findFiles(target, path):
    """
    The function searches for files whose names contain the query.
    The search is performed recursively in all subdirectories of the directories that the given directory contains.

    :param target: Search query
    :param path: Path to the directory to search in
    :return: List of file paths
    """

    resPaths = []
    elements = os.listdir(path)

    for element in elements:
        elementPath = os.path.join(path, element)

        if os.path.isdir(elementPath):
            resPaths += findFiles(target, elementPath)

        else:
            if target in element:
                resPaths.append(elementPath)

    return resPaths


def main():
    path = os.getcwd()
    while True: 
        print(os.getcwd())
        print(MENU)

        command = acceptCommand()

        if command is not None:
            runCommand(command)

        if command is None:
            print('Неверный номер команды.')

        #if command == VIEW:
        
        if command == UP:
            moveUp()

        if command == DOWN:
            moveDown(path)

        if command == NUM:
            print(countFiles(path))

        if command == SIZE:
            print(countBytes(path))

        #if command == FIND:

        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()


