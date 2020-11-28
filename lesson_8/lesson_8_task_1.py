# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

from hashlib import sha256


def count_sub_string(sting):
    assert sting  # По условию (озвученному на лекции) строка должна быть не пустая
    len_string = len(sting)
    count = 0
    hash_set = set()
    for delta in range(len_string - 1):  # -1 т.к. полную строку не учитываем.
        for index in range(len_string - delta):
            ss = ''.join(sting[index] for index in range(index, index + delta + 1))  #
            hash_ss = sha256(ss.encode('utf-8')).hexdigest()
            if hash_ss not in hash_set:
                count += 1
                hash_set.add(hash_ss)
    return count


if __name__ == '__main__':
    s = input('Ведите строку: ')
    print(count_sub_string(s))

# 1) abcde : 14
# 2) aaaaa : 4
# 3) abacabadabacaba : 84
# 4) abc : 5
# 5) abcd : 9
