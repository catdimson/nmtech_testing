# Задача 1
#
# Имеем dictionary со следующей структурой и данными:
# d = {
#     "a": 5,
#     "b": 6,
#     "c": {
#         "f": 9,
#         "g": {
#             "m": 17,
#             "n": 3
#         }
#     }
# }
# Необходимо написать функцию flatten(d), которая на
# входе получает dictionary с указанной выше структурой и
# возвращает dictionary вида:
#     {
#         'a': 5,
#         'b': 6,
#         'c.f': 9,
#         'c.g.m': 17,
#         'c.g.n': 3
#     }
# Алгоритм должен работать для общего случая, т.е. превращать любой многоуровневый
# dictionary в одноуровневый, с ключами, как указано выше.


d = {
    "a": 5,
    "b": 6,
    "c": {
        "f": 9,
        "g": {
            "m": 17,
            "n": 3
        },
        "h": 10
    },
    "i": 33,
    "e": {
        "t": 40,
        "w": 41
    }
}


def flatten(d):
    result = {}

    def flatten2(dic, parent=True):

        local_dict = dict()
        for key in dic.keys():
            if isinstance(dic[key], dict):
                r = flatten2(dic[key], parent=True)
                local_keys = r.keys()
                # print(local_keys) # point 1
                for k in local_keys:
                    local_dict[key + '.' + k] = r[k]
                # print(f"local_dict: {local_dict}") # point 2
                if parent and (key == list(dic.keys())[-1]):
                    return local_dict
                if not parent:
                    result.update(local_dict)
                    # print(f"result: {result}") # point 4
                #
            else:
                if not parent:
                    result[key] = dic[key]
                else:
                    local_dict[key] = dic[key]
        if parent:
            # print("local_dict: {}".format(local_dict)) # point 3
            return local_dict

    flatten2(d, parent=False)

    return result

print(flatten(d))
