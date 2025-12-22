while True:
    case = input()
    if case == "0 0 0":
        break
    s1, s2, s3 = case.split()
    a1, a2, a3 = int(s1), int(s2), int(s3)
    if a2**2 == a1 * a3:
        print(f"GP {a2 * a3 // a1}")
    else:
        print(f"AP {a2 + a3 - a1}")
