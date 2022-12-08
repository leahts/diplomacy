#Takes a .csv file and parses the data (customized for map_data.csv)
def parse_file(file):
    updated_file = []
    for line in file:
        new_line = line.replace("\n", "")
        new_line = new_line.split(",")
        new_line[-1] = new_line[-1].split(" ")
        updated_file.append(new_line)
    return updated_file