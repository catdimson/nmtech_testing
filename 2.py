# Задача 2
#
# Необходимо написать алгоритм (приложение, работающее из командной строки), который на входе получает валидный
# XML документ, и возвращает в виде результата максимальную глубину вложенности тегов в данном документе.
# Глубина измеряется в целых числах: 0, 1, 2 и т.д., при этом глубина корневого тэга принимается равной 0.
# При написании алгоритма могут использоваться любые библиотеки для парсинга XML.
# Пример:
# Содержимое XML документа:
# <feed xml:lang='en'>
#     <title>NPBFX</title>
#     <subtitle lang='en'>Programming challenges</subtitle>
#     <link rel='alternate' type='text/html' href='http://npbfx.com/' />
#     <updated>2020-10-28T12:00:00</updated>
# </feed>
# Результат работы алгоритма: 1
# В данном примере тэг feed имеет глубину вложения: 0. Тэги title, subtitle, link и updated: 1. Поэтому максимальная
# глубина: 1.

import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()


def measure_depth(root_tree):
    """
    Функция принимает объект корня ElementTree - Element. Производит рекурсивный обход дерева.
    Если глубина оказывается больше, чем max_depth, то в max_depth записывается значение глубины depth.
    """
    max_depth = 0
    if len(root_tree) == 0:
        return max_depth
    else:
        max_depth = 1

    def f(subtree, depth):
        nonlocal max_depth
        for node in subtree:
            # print(node)
            if len(node) > 0:
                f(node, depth + 1)
            else:
                if depth > max_depth:
                    max_depth = depth

    f(root_tree, max_depth)

    return max_depth


print(f"Максимальная глубина: {measure_depth(root)}")

