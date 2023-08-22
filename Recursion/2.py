def count_demons(village_map):
    width = len(village_map[0])
    height = len(village_map)
    demon_count = 0

    for y in range(height):
        for x in range(width):
            if village_map[y][x] == '#':
                demon_count += 1
                village_map = remove_demon(village_map, x, y)

    return demon_count

def remove_demon(village_map, x, y):
    if x >= 0 and y >= 0 and x < len(village_map[0]) and y < len(village_map) and village_map[y][x] == '#':
        village_map[y] = village_map[y][:x] + '.' + village_map[y][x+1:]
        village_map = remove_demon(village_map, x+1, y)
        village_map = remove_demon(village_map, x-1, y)
        village_map = remove_demon(village_map, x, y+1)
        village_map = remove_demon(village_map, x, y-1)
    return village_map

# Get input
width, height = map(int, input("Enter input: ").split())
village_map = [input() for _ in range(height)]

# Calculate and print the result
result = count_demons(village_map)
print(result)
