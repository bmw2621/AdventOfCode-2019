import urllib.request

req = urllib.request.Request(url='https://adventofcode.com/2019/day/3/input')
req.add_header("Cookie", # SESSION COOKIE)
with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')

def get_coordinates(wire):
    """Returns a list of tuples where each tuple is a coordinate which the wire passes through"""
    x = 0
    y = 0
    coords = [(0,0)]

    for instruction in wire:
        direction = instruction[0]
        distance = instruction[1]

        if direction == "U":
            coords += [(x, i) for i in range(y + 1,y + distance + 1)]
            y += distance
        elif direction == "R":
            coords += [(i, y) for i in range(x + 1,x + distance + 1)]
            x += distance
        elif direction == "D":
            coords += [(x, i) for i in range(y - 1,y - distance - 1,-1)]
            y -= distance
        elif direction == "L":
            coords += [(i, y) for i in range(x - 1,x - distance - 1,-1)]
            x -= distance

    return coords


# Clean data
wire1 = data.split("\n")[0]
wire2 = data.split("\n")[1]

wire1 = wire1.split(",")
wire1 = [(i[0], int(i[1:])) for i in wire1]

wire2 = wire2.split(",")
wire2 = [(i[0], int(i[1:])) for i in wire2]

wire1_coords = get_coordinates(wire1)
wire2_coords = get_coordinates(wire2)

# Find the intersection of each of the coordinate lists and remove the origin
intersections = list(set(wire1_coords) & set(wire2_coords))
intersections.remove((0,0))

# Find Manhattan Distance of each intersection from the origin
distances_of_intersections = [abs(i[0]) + abs(i[1]) for i in intersections]

# Print the lowest number in the list of Manhattan Distances
print(min(distances_of_intersections))

