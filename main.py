"Fisher Daniil 100"
"Popov Ivan 100"
"Fedyakin Dmitry 100"

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
    """
    The function will check if the function number is valid.

    :return: If the number is correct, then the team number. If the number is incorrect, then NoneType.
    """

    COMMANDS = [str(x) for x in range(1, 8)]

    command = input('Выберите пункт меню: ')

    if command in COMMANDS:
        return command

    return None

def viewDirs(path):
    """
    The function return all elements in directory

    param path: Path to the directory to search in
    return: List of files
    """
    return os.listdir(path)


def runCommand(command):
    """
    The function determines by the command number which function needs to be performed

    param command: Number of command
    """

    path = os.getcwd()
    if command == '1':
        print(*viewDirs(path))

    elif command == '2':
        moveUp()

    elif command == '3':
        moveDown(path)

    elif command == '4':
        print(countFiles(path))

    elif command == '5':
        print(countBytes(path))

    elif command == '6':
        target = input('Введите запрос для поиска: ')
        result = findFiles(target, path)

        if result == []:
            print('Файлы не найдены!')
        else:
            print('\n'.join(result))


def moveUp():
    """
    The function moves to the directory above
    """

    os.chdir('..')


def moveDown(currentDir):
    """
    The function moves to the directory below

    param currentDir: Current directory
    """

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
    while True: 
        path = os.getcwd()
        print(path)
        print(MENU)

        command = acceptCommand()

        if command is not None:
            runCommand(command)

        if command is None:
            print('Неверный номер команды.')

        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()


