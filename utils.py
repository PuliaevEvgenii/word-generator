from itertools import permutations


def __remove_sym(base_str, sym):
    for i in sym:
        base_str = base_str.replace(i, "")
    return base_str


def duplicate_to_console(func_to_dec):
    def wrapper(path, res):
        print("Результат: ", end="")
        print(__remove_sym(str(res), "{}[]'"))
        func_to_dec(path, res)
    return wrapper


@duplicate_to_console
def write_to_file(path, res):
    with open(path, "w") as output:
        for i in res:
            output.write(str(i) + "\n")


def read_from_file(path):
    with open(path, "r") as input_file:
        res = [line.strip().split() for line in input_file]
        return res


def make_instructions(arr):
    instructions = dict()
    instructions.update({"letters": arr[0]})
    instructions.update({"k": int(__remove_sym(str(arr[1]), "{}[]',"))})
    found = dict()
    if len(arr) > 2:
        for i in arr[2]:
            kv = i.strip().split(':')
            found.update({int(kv[0]) - 1: kv[1]})
    instructions.update({"found": found})
    return instructions


def arr_to_str(arr):
    word = ""
    for i in arr:
        word += i
    return word


def generate_all(arr, k):
    res = set()
    for i in permutations(arr, k):
        res.add(i)
    return res


def remove_extra(arr, lets: dict):
    res = set()
    for word in arr:
        fits = True
        for k, v in lets.items():
            if word[k] != v:
                fits = False
        if fits:
            res.add(word)
    return res
