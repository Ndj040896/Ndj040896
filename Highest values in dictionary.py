# Program to find the 3 highest values from a dictionary:

d = {"a": 1, "b": 5, "c": 7, "d":7, "g":7}

max_keys = max(d.values())

max_value = max(d, key=d.get)

print(max_keys, max_value)
