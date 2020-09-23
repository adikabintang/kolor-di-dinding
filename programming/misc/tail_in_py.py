with open("file.txt", mode="r") as f:
    content = f.readlines()
    for line in content[-4:]:
        print(line, end="")
