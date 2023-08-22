__author__ = 'https://github.com/Flory143'
__version__ = '0.1.0'

import os
import platform
import time
import shutil
from colorama import init
init()
from colorama import Fore

system = platform.uname()
user_name = os.getlogin()
clean_folder = f'C:/Users/{user_name}/Desktop/CleanUp_By_Foxxer'

def main():
    os.system('cls')
    print(f'CleanUP - {__version__} \nCheck updates - {__author__}')

    print('\n1. Safe mode \n2. Full mode (soon...) \n3. Information\n')

    choice = input (Fore.GREEN + 'Press ENTER to exit -> ' + Fore.RESET)

    if choice == '1':
        safety_clean()
    elif choice == '2':
        main()
    elif choice == '3':
        information()
    elif choice == '':
        pass
    else:
        main()

def preparation():
    os.makedirs(clean_folder)

def safety_clean():
    dir_download = os.listdir(f'C:/Users/{user_name}/Downloads')
    dir_temp = os.listdir('C:\Windows\Temp')
    dir_local_temp = os.listdir(f'C:/Users/{user_name}/AppData/Local/Temp')
    dir_prefetch = os.listdir('C:\Windows\Prefetch')
    os.system('cls')
    
    try:
        preparation()
        print(Fore.GREEN + '\nA folder named "CleanUP_By_Foxxer" has been created.' + Fore.RESET)
        time.sleep(1)
    except:
        print(Fore.RED + '\nA folder named "CleanUP_By_Foxxer" has already been created. Please delete it.' + Fore.RESET)
        time.sleep(2)
    
    print(Fore.CYAN + 'All in Downloads' + Fore.RESET)
    for x in dir_download:
        try:
            shutil.move(f'C:/Users/{user_name}/Downloads/{x}', clean_folder)
            print(x + Fore.GREEN + ' - successfully' + Fore.RESET)
        except Exception as e:
            print(x + Fore.RED + ' - error: ' + str(e) + Fore.RESET)
   
    #TEMP
    print(Fore.CYAN + '\nAll in TEMP folder' + Fore.RESET)
    for x in dir_temp:
        try:
            shutil.move(f'C:/Windows/Temp/{x}', clean_folder)
            print(x + Fore.GREEN + ' - successfully moved' + Fore.RESET)
        except Exception as e:
            print(x + Fore.RED + ' - error: ' + str(e) + Fore.RESET)
    
    #Local_TEMP
    print(Fore.CYAN + '\nAll in local TEMP folder' + Fore.RESET)
    for x in dir_local_temp:
        try:
            shutil.move(f'C:/Users/{user_name}/AppData/Local/Temp/{x}', clean_folder)
            print(x + Fore.GREEN + ' - successfully moved' + Fore.RESET)
        except Exception as e:
            print(x + Fore.RED + ' - error: ' + str(e) + Fore.RESET)
    
    #Prefetch
    print(Fore.CYAN + '\nAll in Prefetch folder' + Fore.RESET)
    for x in dir_prefetch:
        try:
            shutil.move(f'C:\Windows/Prefetch\{x}', clean_folder)
            print(x + Fore.GREEN + ' - successfully moved' + Fore.RESET)
        except Exception as e:
            print(x + Fore.RED + ' - error: ' + str(e) + Fore.RESET)
    
    confirm = input('\nDo you want to preview files before deleting? (' + Fore.GREEN +'y' + Fore.RESET +' / ' + Fore.RED +'n' + Fore.RESET + ') ')
    
    if confirm == 'y':
        os.system('cls')

        print(Fore.CYAN + 'Preview\n' + Fore.RESET)

        clean_folder_clear = os.listdir(clean_folder)
        for x in clean_folder_clear:
            print(x)

        confirm_2 = input('\nAre you sure you want to delete everything? (' + Fore.GREEN +'y' + Fore.RESET +' / ' + Fore.RED +'n' + Fore.RESET + ') ')

        if confirm_2 == 'y':
            delete_file_from_desktop()
    elif confirm == 'n':
        delete_file_from_desktop()
    else:
        print('Okey, all your files are on the desktop in the folder "CleanUp_By_Foxxer"')
        print('3 sec')
        time.sleep(3)
        print('2 sec')
        time.sleep(2)
        print('1 sec')
        time.sleep(1)
        main()

    try:
        os.startfile(clean_folder)
        print(Fore.RED + '\nYou have run this application as an administrator, please delete this file after exiting the application.' + Fore.RESET)
    except:
        input (Fore.RED + '\nIf the program was run as administrator, then after closing it, delete the folder - C:\\Users\\dima1\\Desktop\\CleanUp_By_Foxxer -> ' + Fore.RESET)

    input (Fore.GREEN + '\nPress ENTER to return to the menu -> ' + Fore.RESET)

    main()

def delete_file_from_desktop():
    amount = 0

    os.system('cls')
    print(Fore.CYAN + 'Deleted files' + Fore.RESET)

    try:
        clean_folder_clear = os.listdir(clean_folder)
    except Exception as e:
        print(f"Error reading directory: {e}")

    for x in clean_folder_clear:
        amount += 1
        try:
            print(x + Fore.GREEN + ' - successfully deleted' + Fore.RESET)
        except Exception as e:
            print(print(x + Fore.RED + ' - error: ' + str(e) + Fore.RESET))
    
    try:
        shutil.rmtree(clean_folder)
    except Exception as e:
        print('Error: ' + str(e))

    print(f'\n{Fore.YELLOW} {amount} file(s) have been deleted {Fore.RESET}')

def information():
    os.system('cls')

    print(Fore.CYAN + 'Information\n' + Fore.RESET)
    print(f'This script was writen by {__author__}')
    print(f'Version - {__version__}')
    print('\nThe program was written for people who are too lazy to clean their PC manually.')
    print('Safe mode - is needed for cleaning with temporary saving and external confirmation.')
    print('Full mode - is needed for a more severe cleaning.\n')

    print(f"System: {system.system}; \nPC: {system.node}; \nUser: {user_name}\n")

    input (Fore.GREEN + '\nPress ENTER to return to the menu -> ' + Fore.RESET)

    main()

if __name__ == '__main__':
    main()