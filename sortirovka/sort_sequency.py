def parcer_condition(cond: str) -> str:
    """Проверка валидности условия."""
    operators = []  # Список хранения операторов
    objects = []  # Список хранения объектов

    cond = cond.replace(' ', '')  # Избавляемся от пробелов
    finded_operator = ''
    flag = 0
    len_cond = len(cond)

    # Формируем списки объектов и операторов. Проверяем строгость условий.
    for i in range(len_cond):

        if cond[i] == '<' or cond[i] == '>':

            if finded_operator == '':
                finded_operator = cond[i]

            if cond[i] == finded_operator:
                operators.append(cond[i])
                objects.append(cond[flag:i])
            else:
                return False

            flag = i+1

        elif cond[i] == '=':
            return False

    # Добавляется последний эллемент
    objects.append(cond[flag:len_cond])

    # Если не нашелся ни один оператор сравнения
    if finded_operator == '' or '' in objects:
        return False

    # Все условия определенны однозначно
    if len(set(objects)) - len(operators) != 1:
        return False

    parc_len = len(objects)
    dic = {}

    if finded_operator == '<':
        for i in range(parc_len):
            dic[objects[i]] = i

    else:
        for i in range(parc_len):
            dic[objects[i]] = parc_len - i

    return dic


def check_input(data: str, cond: str) -> list:
    """Проверка входных параметров на основании условий."""

    condition = parcer_condition(cond)

    if not condition:
        print('Ошибка создания условия')
        return False
    # Если словарь создан, Забираем ключи и разбиваем входную строку

    if ' ' not in data:
        print('Нет объектов для сорировки')
        return False

    parcer_str = data.split(' ')

    # Избавляемся от лишних пробелов

    parcer_str = [elem for elem in parcer_str if elem != '']

    if len(parcer_str) <= 1:
        return False

    keys = condition.keys()

    # Проверяем, все ли эллементы входной строки мы сможет отсортировать
    for i in parcer_str:
        if i not in keys:
            print('Полученные данные не удовлетворяют условиям сортировки')
            return False

    result = [parcer_str, condition]
    return result


def sort_input(data: str, cond: str) -> str:
    """Основная функция сортировки входных данных по условию."""
    temp_list = []
    sorted_str = ''
    input = check_input(data, cond)

    if not input:
        return False

    objects = input[0]  # Входные данные
    condition = input[1]  # Словарь условий

    # Заменяем буквы их весами
    for i in objects:
        temp_list.append(condition.get(i))

    # Сортируем
    temp_list.sort()
    # Делаем обратную замену от цифр к буквам и соединяем в строку
    for i in range(len(temp_list)):
        for key, value in condition.items():
            if temp_list[i] == value:
                if i == len(temp_list)-1:
                    sorted_str += str(key)
                else:
                    sorted_str += str(key)+' '

    return sorted_str


condition = 'З<С<К'
input = 'С С З С К З З З К К С З С С К З'
print(sort_input(input, condition))
