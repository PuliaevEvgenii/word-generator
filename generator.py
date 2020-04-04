import sys

import pymorphy2

from utils import write_to_file, generate_all, remove_extra, read_from_file, arr_to_str, make_instructions

if __name__ == "__main__":
    instr = {}

    if sys.argv.__contains__('-i'):
        attrs = list()
        print("Введите используемые символы: ", end="")
        letters = input()
        attrs.append(letters.strip().split())
        print("Введите длину искомого слова: ", end="")
        k = int(input())
        attrs.append([k])
        print("Введите уже найденные символы [номер_символа:символ]: ", end="")
        found_letters = input()
        if len(found_letters) > 0:
            attrs.append([found_letters])
        instr = make_instructions(attrs)
    else:
        instr = make_instructions(read_from_file("input"))

    letters = instr.get("letters")
    k = instr.get("k")
    found_letters = instr.get("found")
    possible_words = [arr_to_str(i) for i in sorted(remove_extra(generate_all(letters, k), found_letters))]

    morph = pymorphy2.MorphAnalyzer()
    res = set()
    for word in possible_words:
        if morph.word_is_known(word):
            res.add(word)

    write_to_file("output", res)
