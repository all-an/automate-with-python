
street_intersection1 = {
    'north_south': 'green',
    'east_west': 'red'
}

def switch_traffic_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'neither light is red' + str(intersection)

print(street_intersection1)

switch_traffic_lights(street_intersection1)

print(street_intersection1)