data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def func_calculate(data):
    total = 0
    if isinstance(data, (int, float)):
        total += data

    elif isinstance(data, str):
        total += len(data)

    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += func_calculate(item)

    elif isinstance(data, dict):
        for key, value in data.items():
            total += func_calculate(key)
            total += func_calculate(value)

    return total

result = func_calculate(data_structure)

print(func_calculate(data_structure))






















