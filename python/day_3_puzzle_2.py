import urllib.request

req = urllib.request.Request(url='https://adventofcode.com/2019/day/3/input')
req.add_header("Cookie", "session=53616c7465645f5ff85d2293bbb71faf9caeca66488104faf5a9521d283e71820d260467637fc8429493184cdd9a020c")
with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')
# data = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"

def get_coordinates(wire):
    """Returns a list of tuples where each tuple is a coordinate which the wire passes through and an enumeration of the same list"""
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

    coords_step = list(enumerate(coords))[1:]

    return coords, coords_step


# Clean data
wire1 = data.split("\n")[0]
wire2 = data.split("\n")[1]

wire1 = wire1.split(",")
wire1 = [(i[0], int(i[1:])) for i in wire1]

wire2 = wire2.split(",")
wire2 = [(i[0], int(i[1:])) for i in wire2]

wire1_coords, wire1_coords_enum = get_coordinates(wire1)
wire2_coords, wire2_coords_enum = get_coordinates(wire2)

# Find the intersections
intersections = list(set(wire1_coords) & set(wire2_coords))

step_counter = []

# For each intersection, find the first occurrence along each wire and append sum to list
for intersection in intersections:
    for coord1 in wire1_coords_enum:
        if coord1[1] == intersection:
            break
    for coord2 in wire2_coords_enum:
        if coord2[1] == intersection:
            break
    step_counter.append(coord1[0] + coord2[0])

# Return lowest sum of counts in the storage list
print(min(step_counter))
