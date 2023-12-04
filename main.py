import os

MENU = '1. Просмотр каталога \n2. На уровень вверх \n3. На уровень вниз \n4. Количество файлов и каталогов \n5. Размер текущего каталога (в байтах) \n6. Поиск файла \n7. Выход из программы \nВыбери пункт меню'

def main(): 
    while True: 
        print (os.getcwd()) 
        print (MENU) 
        command = acceptCommand() 
        runCommand(command) 
        if command == QUIT: 
            print ('Работа программы завершена.') 
            break
        
if __name__ == '__main__':
    main()