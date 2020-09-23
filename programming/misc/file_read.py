with open("sample.txt", mode="r") as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

        