# Типы переменных

obj = 'Server'  # Объект Сервер
print('{:>20} {:<7} {}'.format('Объект:', obj, type(obj)))

name = 'Baikal'  # Название
print('{:>20} {:<7} {}'.format('Название:', name, type(name)))

CUDO = True  # Наличие CUDO: есть или нет?
print('{:>20} {:<7} {}'.format('Наличие CUDO:', CUDO, type(CUDO)))

GPU = 10784  # Количество ядер CUDO
print('{:>20} {:<7} {}'.format('Количество ядер GPU:', GPU, type(GPU)))

Disk = 192.46  # Объем диска Системы в GB
print('{:>20} {:<7} {}'.format('Объем диска [GB]:', Disk, type(Disk)))

Start = False  # Сервер запущен?
print('\n Сервер уже запущен?', Start, type(Start))
