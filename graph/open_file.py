def open_file(file):
    for line in file:
        line = line.replace("\n", "")
        line = line.split(",")
        line[-1] = line[-1].split(" ")
    return file