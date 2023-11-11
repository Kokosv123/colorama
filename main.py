from colorama import Fore, Back, Style, init, deinit
init(autoreset=True)  # Инициализация colorama для автоматического сброса цвета после каждого вывода

#самые важые атрибуты/методы
print(Fore.RED + 'красный текст') # делает текст красный
print(Back.GREEN + 'зеленый бэк.')# теперь текст с зеленым бэккраудном
print(Style.DIM + 'тусклый') # делает текст тусклым
print(Style.RESET_ALL) # перезапускает
print(Style.BRIGHT + Fore.BLUE + 'Это яркий синий текст')# цвет ярко синий
print('теперь все нормально')
deinit()  # Деинициализация colorama