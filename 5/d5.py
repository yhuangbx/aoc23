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


seeds2=[]
i = 0
while i < len(seeds):
    seeds2+=list(range(seeds[i],seeds[i]+seeds[i+1]))
    i += 2

seeds2 = list(set(seeds2))
print(seeds2)
result2 = defaultdict(int)

for seed in seeds2:
    # print("seed: {}".format(seed))
    soil = find_mappings(mappings['seed-to-soil'],seed)
    # print("soil: {}".format(soil))
    fertilizer = find_mappings(mappings['soil-to-fertilizer'],soil)
    water = find_mappings(mappings['fertilizer-to-water'],fertilizer)
    light = find_mappings(mappings['water-to-light'],water)
    temperature = find_mappings(mappings['light-to-temperature'],light)
    humidity = find_mappings(mappings['temperature-to-humidity'],temperature)
    location = find_mappings(mappings['humidity-to-location'],humidity)
    result2[seed] = location

print(min(result2.values()))
# print(min(result2, key=result2.get))