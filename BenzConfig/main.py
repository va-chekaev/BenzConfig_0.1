from colorama import init, Fore

init(autoreset=True)


a = float(input('Введите пройденный километраж: '))
print()

print(Fore.YELLOW + 'Летний')

print('Вы потратили по городу', Fore.CYAN + str(round(0.3 * a / 100 * 11.5, 2)), 'литров')
print("Вы потратили по трассе", Fore.CYAN + str(round(0.7 * a / 100 * 8.5, 2)), 'литров\n')

print('Общий расход бензина:', Fore.CYAN + str(round((0.3 * a / 100 * 11.8) + (0.7 * a / 100 * 8.5), 2)), 'литров')
print('Расход 11.5 / 8.5 л. на 100 км.\n')

print(Fore.BLUE + 'Зимний')

print('Вы потратили по городу', Fore.CYAN + str(round(0.3 * a / 100 * 13.8, 2)), 'литров')
print("Вы потратили по трассе", Fore.CYAN + str(round(0.7 * a / 100 * 10.2, 2)), 'литров\n')

print('Общий расход бензина:', Fore.CYAN + str(round((0.3 * a / 100 * 13.8) + (0.7 * a / 100 * 10.2), 2)), 'литров')

print('Расход 13.8 / 10.2 л. на 100 км.\n')

input("Нажмите Enter для закрытия программы")
