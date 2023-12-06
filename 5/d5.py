import sys
from collections import defaultdict


D = open(sys.argv[1]).read().strip()
lines = D.split('\n')


# seed_to_soil = []
# soil_to_fertilizer = []
# fertilizer_to_water = []
# water_to_light = []
# light_to_temperature = []
# termperature_to_humidity = []
# humidity_to_location = []
mappings = {}

def find_mappings(map,number):
    ans = number
    for x in map:
        if number in range(x[1],x[1]+x[2]):
            ans = number - x[1] + x[0]
    return ans

for line in lines:
    line = line.strip()
    if not line:
        continue
    if ':' in line:
        current_key = line.split(':')[0].strip()
        if current_key == 'seeds':
            seeds=list(map(int,line.split(':')[1].strip().split()))
        else:
            current_key = current_key.split()[0]
            mappings[current_key] = []
    else:
        values = list(map(int, line.split()))
        mappings[current_key].append(values)

result = []

for seed in seeds:
    # print("seed: {}".format(seed))
    soil = find_mappings(mappings['seed-to-soil'],seed)
    # print("soil: {}".format(soil))
    fertilizer = find_mappings(mappings['soil-to-fertilizer'],soil)
    water = find_mappings(mappings['fertilizer-to-water'],fertilizer)
    light = find_mappings(mappings['water-to-light'],water)
    temperature = find_mappings(mappings['light-to-temperature'],light)
    humidity = find_mappings(mappings['temperature-to-humidity'],temperature)
    location = find_mappings(mappings['humidity-to-location'],humidity)
    result.append(location)


print(min(result))


seeds2 = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]
seeds2 = [[sublist[0], sublist[0] + sublist[1] - 1] for sublist in seeds2]

print(seeds2)
result2 = defaultdict(int)

def find_intersaction(range1, range2):
    a, b = range1
    c, d = range2
    # Find the intersection
    intersection_start = max(a, c)
    intersection_end = min(b, d)

    # Check if there is a valid intersection
    if intersection_start <= intersection_end:
        return range(intersection_start, intersection_end+1)
    else:
        return None
    
for seed in seeds2:
    for x in mappings['seed-to-soil']:
        r = find_intersaction(seed, [x[1],x[1]+x[2]-1])
        if r is not None:
            r = list(range(r[0],r[1]))
            print(r)
            for v in r:
                soil = find_mappings(mappings['seed-to-soil'],v)
                fertilizer = find_mappings(mappings['soil-to-fertilizer'],soil)
                water = find_mappings(mappings['fertilizer-to-water'],fertilizer)
                light = find_mappings(mappings['water-to-light'],water)
                temperature = find_mappings(mappings['light-to-temperature'],light)
                humidity = find_mappings(mappings['temperature-to-humidity'],temperature)
                location = find_mappings(mappings['humidity-to-location'],humidity)
                result2[v] = location

print(min(result2.values()))
# print(min(result2, key=result2.get))