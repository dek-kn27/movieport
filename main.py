import os.path
import json
import re
import folium
import geocoder



MESSAGE_GETMAP_INPUT = 'Enter year: '
MESSAGE_GETMAP_NOMOVIES = 'No movies shoot this year. Press Enter to exit. '
MESSAGE_GETMAP_DONE = 'Done to map.html. Press Enter to exit. '

FILENAME_LIST_LOCATIONS = 'locations.list'
FILENAME_JSON_LOCATIONS = 'locations.json'
FILENAME_HTML_RESULTGEOMAP = 'map.html'

REGEXP_LINE = r'^".*" \((\d+)\)[^\t]*\t+([^\t]+)'

MAPS_API_KEY = 'At3AyKtDPtkovQwtGL5yqPzuxbnu_siJ6fWeJu8gDJsWCtQ6jeHZpwdQqwM1p9s0'


def input_year(message):
    try:
        return int(input(message))
    except:
        return 0


def create_json_file(input_filename, output_filename):
    input_file = open(input_filename, 'r')
    while input_file.readline() != '==============\n':
        pass
    venues = {}
    line = ''
    while True:
        line = input_file.readline().strip('\n')
        if line == '--------------------------------------------------------------------------------':
            break
        else:
            match = re.match(REGEXP_LINE, line)
            if match:
                groups = match.groups()
                key = groups[0]
                if key not in venues:
                    venues[key] = set()
                venues[key].add(groups[1])
    input_file.close()
    for key in venues:
        venues[key] = list(venues[key])
    with open(output_filename, 'w') as output_file:
        json.dump(venues, output_file)


def get_coordinates(addresses):
    print('in')
    print(len(addresses))
    coords = []
    num_slices_and_rest = divmod(len(addresses), 50)
    for i in range(num_slices_and_rest[0]):
        print('in2')
        coords.extend([venue.latlng for venue in geocoder.bing(addresses[50 * i : 50 * (i + 1)], method='batch', key=MAPS_API_KEY)])
    coords.extend([venue.latlng for venue in geocoder.bing(addresses[len(addresses) - num_slices_and_rest[1] : len(addresses)], method='batch', key=MAPS_API_KEY)])
    return coords


def main():
    year = 0
    while not year:
        year = input_year(MESSAGE_GETMAP_INPUT)
    if not os.path.isfile(FILENAME_JSON_LOCATIONS):
        create_json_file(FILENAME_LIST_LOCATIONS, FILENAME_JSON_LOCATIONS)
    f = open(FILENAME_JSON_LOCATIONS, 'r')
    json_data = f.read()
    f.close()
    venues = json.loads(json_data)
    year = str(year)
    if year not in venues:
        input(MESSAGE_GETMAP_NOMOVIES)
    else:
        map = folium.Map()
        venues_list = venues[year]
        coords = get_coordinates(venues_list)
        for i in range(len(venues_list)):
            folium.Marker(coords[i], popup=venues_list[i]).add_to(map)
        map.save(FILENAME_HTML_RESULTGEOMAP)
        print(FILENAME_HTML_RESULTGEOMAP)



#create_json_file('locations.list', 'locations.json')

main()