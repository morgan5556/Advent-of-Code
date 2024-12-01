def read_file(year, day):
    file = open(f"{year}/inputs/{day}.txt", "r")
    content = file.read()
    file.close()

    return content