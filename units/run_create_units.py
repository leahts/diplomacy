#Imports
from creating_units import update_map
from creating_units import create_unit

def run_create_units(units_to_create, map_file, image_file):
    i = 0
    num_of_units = len(units_to_create)
    while i < num_of_units:
        country = units_to_create[i][0]
        territory = units_to_create[i][1]
        unit_type = units_to_create[i][2][0]
        if i == 0:
            unit = create_unit(country, territory, unit_type, map_file, image_file)
            unit_on_map = unit.create_unit_symbol()
        else:
            prev_country = units_to_create[i - 1][0]
            prev_territory = units_to_create[i - 1][1]
            prev_unit_type = units_to_create[i - 1][2][0]
            previous_unit = create_unit(prev_country, prev_territory, prev_unit_type, map_file, unit_on_map)
            previous_map = previous_unit.create_unit_symbol()
            unit = create_unit(country, territory, unit_type, map_file, previous_map)
            unit_on_map = unit.create_unit_symbol()
        i += 1
    return unit_on_map