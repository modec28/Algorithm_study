codes = input().split()

def check():
    for index in range(1, len(codes)):
        if abs(int(codes[index-1]) - int(codes[index])) > 1:
            return "mixed"
    if codes[0] == "1":
        return "ascending"
    return "descending"

if __name__ == "__main__":
    print(check())