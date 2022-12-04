#Takes a .csv file and parses the data (customized for map_data.csv)
def parse_file(file):
    for line in file:
        line = line.replace("\n", "")
        line = line.split(",")
        line[-1] = line[-1].split(" ")
    return file