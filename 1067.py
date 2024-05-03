def create_structure(ways):
    # функция по созданию структуры
    # создаем словарь, который представляет из себя структуру папок
    structure = {}
    for way in ways:
        # создаем массив с названиями папками
        folders = way.split('\\')
        current_folder = structure
        for folder in folders:
            if folder not in current_folder:
                # если папки еще не было в нашей структуре
                current_folder[folder] = {}
            # переходим на уровень ниже
            current_folder = current_folder[folder]
    # возвращаем структуру
    return structure


def display_folder_structure(structure, level=0):
    for folder, sub_folders in sorted(structure.items()):
        # печатаем папку
        print(' ' * level + folder)
        # переходим в папки уровня ниже
        display_folder_structure(sub_folders, level + 1)


# считываем данные
n = int(input())
paths = [input() for _ in range(n)]
# отрпавляем полученные данные в функции
display_folder_structure(create_structure(paths))

