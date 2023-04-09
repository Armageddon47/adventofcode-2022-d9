def differ_by_zero_or_one(a, b):
    return abs(a - b) <= 1
print(differ_by_zero_or_one(2, 3))   # output: True
print(differ_by_zero_or_one(-1, 0))  # output: True
print(differ_by_zero_or_one(4, 7))   # output: False