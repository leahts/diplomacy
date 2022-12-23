#Takes a .csv file and parses the data (customized for map_data.csv)
def parse_moves(file):
    file = file.readlines()[1:]
    updated_file = []
    for line in file:
        new_line = line.replace("\n", "")
        new_line = new_line.split(",")
        updated_file.append(new_line)
    return updated_file