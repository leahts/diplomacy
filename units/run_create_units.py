#Imports
from unit_class import update_map
from unit_class import Unit

def run_create_units(units_to_create, map_file, image_file, return_type):
    i = 0
    num_of_units = len(units_to_create)
    all_units = []
    while i < num_of_units:
        country = units_to_create[i][0]
        territory = units_to_create[i][1]
        unit_type = units_to_create[i][2][0]
        if i == 0:
            unit = Unit(country, territory, i, unit_type, map_file, image_file)
            unit_on_map = unit.create_unit_symbol()
            all_units.append(unit)
        else:
            prev_country = units_to_create[i - 1][0]
            prev_territory = units_to_create[i - 1][1]
            prev_unit_type = units_to_create[i - 1][2][0]
            previous_unit = Unit(prev_country, prev_territory, i, prev_unit_type, map_file, unit_on_map)
            previous_map = previous_unit.create_unit_symbol()
            unit = Unit(country, territory, i, unit_type, map_file, previous_map)
            unit_on_map = unit.create_unit_symbol()
            all_units.append(unit)
        i += 1
    if return_type == "units":
        return all_units
    elif return_type == "updated map":
        return unit_on_map