# 2) Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heap_node_append(h_lst, node):
    """добавляет элемент в список и восстанавливает структуру мин-кучи"""
    assert isinstance(h_lst, list)  # Работает только с list
    h_lst.append(node)
    index = len(h_lst) - 1
    while index > 0:
        if h_lst[index // 3].value <= h_lst[index].value:
            break
        h_lst[index], h_lst[index // 3] = h_lst[index // 3], h_lst[index]
        index = index // 3
    return


def heap_node_pop(h_list):
    """ извлекает минимальный элемент и восстанавливает структуру мин-кучи"""
    h_list[0], h_list[-1] = h_list[-1], h_list[0]
    elem = h_list.pop()
    index = 0
    while index * 2 + 2 <= len(h_list) - 1:
        if h_list[index].value > h_list[index * 2 + 2].value or h_list[index].value > h_list[index * 2 + 1].value:
            if h_list[index * 2 + 1].value <= h_list[index * 2 + 2].value:
                h_list[index], h_list[index * 2 + 1] = h_list[index * 2 + 1], h_list[index]
                index = index * 2 + 1
            else:
                h_list[index], h_list[index * 2 + 2] = h_list[index * 2 + 2], h_list[index]
                index = index * 2 + 2
        else:
            return elem
    if index * 2 + 1 <= len(h_list) - 1:
        if h_list[index].value > h_list[index * 2 + 1].value:
            h_list[index], h_list[index * 2 + 1] = h_list[index * 2 + 1], h_list[index]
    return elem


def huf_tree(string):
    """создает дерево Хаффмана на основе входной строки"""
    freq_dict = Counter(string)
    h_list = []  # буду использовать очередь с приорететами (min-кучу), где сортировка будет осущ. на основе частот...
    while freq_dict:
        item = freq_dict.popitem()
        heap_node_append(h_list, MyNode(item[1], item[0]))
    while len(h_list) > 1:
        min_nod_1 = heap_node_pop(h_list)
        min_nod_2 = heap_node_pop(h_list)
        new_nod = MyNode(min_nod_1.value + min_nod_2.value,
                         min_nod_1 if min_nod_1.right else min_nod_1.left,
                         min_nod_2 if min_nod_2.right else min_nod_2.left)
        heap_node_append(h_list, new_nod)
    return h_list.pop()


def huf_cod(h_tree, cod=None, symbol_cod=''):
    """Создает таблицу кодирования Хаффмана(в виде словаря) на основе дерева Хаффмана"""
    cod = cod or {}
    if isinstance(h_tree, str):
        cod[h_tree] = symbol_cod
        return cod
    if h_tree.left:
        cod.update(huf_cod(h_tree.left, cod, symbol_cod + '0'))
    if h_tree.right:
        cod.update(huf_cod(h_tree.right, cod, symbol_cod + '1'))
    return cod


def huf_coding(string):
    """Возвращает список из закодированной строки и таблицы кодирования"""
    if len(string) <= 1:
        return ['0', {string: '0'}]
    tree = huf_tree(string)
    cod = huf_cod(tree)
    code_string = ''.join(cod[i] for i in string)  # для примера из методички - ' '.join(), но для декод. это лишнее
    return [code_string, cod]


def encode_haf(string, code):
    """Осуществляет декодирование зашифрованной строки(string) согласно таблице кодирования(code)"""
    encode = {key: val for val, key in code.items()}
    encode_string = ''
    item = ''
    for i in string:
        item += i
        if item in encode:
            symbol = encode[item]
            encode_string += symbol
            item = ''
    return encode_string


def test_haf_cod(n_iter=10, min_len_string=0, max_len_string=1000000):
    """тестирует работоспособность функции huf_coding()"""
    from random import randint  # Расчитываю получить ответ, на сколько допустимо таким образом имортитровать...?
    for _ in range(n_iter):
        test_string = ''.join((chr(randint(32, 255)) for _ in range(randint(min_len_string, max_len_string))))
        # print(test_string)
        code_test_string, schiff = huf_coding(test_string)
        # print(code_test_string, schiff)
        encode_test_string = encode_haf(code_test_string, schiff)
        # print(encode_test_string)
        if test_string != encode_test_string:
            print('!!!!!ОЙ БЯДА, БЯДА, ОГОРЧЕНИЕ!!!!!', test_string, encode_test_string, sep='\n')
            return
    print('Ок!')


if __name__ == '__main__':
    s = input('Введите строку: ')
    arh, cod_dict = huf_coding(s)
    print(arh)
    # print(encode_haf(arh, cod_dict))
    # test_haf_cod()

# Алексей, спасибо Вам огромное!!!
# Это было, прям, вот, КРУТО!...
# я не про вычисление по IP :o) ...ну, не только про вычисление по IP...
