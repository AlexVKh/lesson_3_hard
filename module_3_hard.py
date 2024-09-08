def calculate_structure_sum(*args):
    n = 0
    list_ = list(*args)
    for i in range(len(list_)):
        if isinstance(list_[i], int):
            n += list_[i]
        elif isinstance(list_[i], str):
            n += len(list_[i])
        elif isinstance(list_[i], dict):
            n += calculate_structure_sum(list_[i].items())
        else:
            n += calculate_structure_sum(list_[i])
    return n

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
