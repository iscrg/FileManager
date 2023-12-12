"""
Fisher Daniil 100
Popov Ivan 100
Fedyakin Dmitry 100
"""

import os
import ru_local


COMMANDS = [str(x) for x in range(1, 8)]
QUIT = '7'


def acceptCommand():
    """
    The function will check if the function number is valid.

    :return: If the number is correct, then the team number. If the number is incorrect, then NoneType.
    """

    command = input(ru_local.CHOOSE_MENU)

    if command in COMMANDS:
        return command

    return None


def viewDirs(path):
    """
    The function return all elements in directory.

    :param path: Path to the directory to search in
    :return: List of files
    """

    return os.listdir(path)


def runCommand(command):
    """
    The function determines by the command number which function needs to be performed.

    :param command: Number of command
    """

    path = os.getcwd()
    if command == '1':
        print('\n'.join(viewDirs(path)))

    elif command == '2':
        moveUp()

    elif command == '3':
        moveDown(path)

    elif command == '4':
        print(countFiles(path))

    elif command == '5':
        print(countBytes(path))

    elif command == '6':
        target = input(ru_local.TYPE_IN_SEARCH)
        result = findFiles(target, path)

        if not result:
            print(ru_local.FILES_NOT_FOUND)
        else:
            print('\n'.join(result))


def moveUp():
    """
    The function moves to the directory above.
    """

    os.chdir('..')


def moveDown(currentDir):
    """
    The function moves to the directory below.

    :param currentDir: Current directory
    """

    subDir = input(ru_local.TYPE_IN_CATALOG)
    elementPath = os.path.join(currentDir, subDir)

    if os.path.isdir(elementPath):
        os.chdir(subDir)

    else:
        print(ru_local.INVALID_NAME)


def countFiles(path):
    """
    The function counts the number of files in the directory.

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
    The function calculates the total volume of files in a directory in Bytes.

    :param path: Path to the directory to search in
    :return: the total volume of files in a directory in Bytes
    """
        
    amount_bytes = 0
    elements = os.listdir(path)

    for element in elements:
        elementPath = os.path.join(path, element)

        if os.path.isfile(elementPath):
            amount_bytes += os.path.getsize(elementPath)

        else:
            amount_bytes += countBytes(elementPath)
    
    return amount_bytes


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
        print(ru_local.CURRENT_DIRECTORY, path)
        print(ru_local.MENU)

        command = acceptCommand()

        if command is not None:
            runCommand(command)

        if command is None:
            print(ru_local.INVALID_COMMAND)

        if command == QUIT:
            print(ru_local.SHUTDOWN)
            break


if __name__ == '__main__':
    main()
