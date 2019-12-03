import urllib.request

req = urllib.request.Request(url='https://adventofcode.com/2019/day/2/input')
req.add_header("Cookie", # SESSION COOKIE)
with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')

# Clean data
data.replace("\n","")
data = data.split(",")
data = [int(i) for i in data]

# Update to last state as per instructions
data[1], data[2] = (12, 2)

idx = 0

while True:
    operation, pos1, pos2, write_pos = (data[idx], data[idx + 1], data[idx + 2], data[idx + 3])

    if operation == 99:
        break
    elif operation == 1:
        # Adding operation
        data[write_pos] = data[pos1] + data[pos2]
    elif operation == 2:
        # Multiplication operation
        data[write_pos] = data[pos1] * data[pos2]
    else:
        print(f"Unkonwn Operation: {operation}")

    idx += 4

print(data)