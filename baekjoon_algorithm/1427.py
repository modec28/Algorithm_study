val = input()
val = list(map(str, val))
val = sorted(val, reverse=True)
print("".join(val))