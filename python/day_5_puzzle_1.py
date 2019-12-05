import urllib.request

req = urllib.request.Request(url='https://adventofcode.com/2019/day/5/input')
req.add_header("Cookie", "session=53616c7465645f5ff85d2293bbb71faf9caeca66488104faf5a9521d283e71820d260467637fc8429493184cdd9a020c")
with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')

# Clean data
data.replace("\n","")
data = data.split(",")
data = [int(i) for i in data]


idx = 0

while True:
    operation, pos1, pos2, pos3 = (data[idx], data[idx + 1], data[idx + 2], data[idx + 3])

    operation = str(operation).zfill(5)
    param3, param2, param1, opcode = [int(operation[0]), int(operation[1]), int(operation[2]), int(operation[3] + operation[4])]

    value1 = data[pos1] if param1 == 0 else pos1
    value2 = data[pos2] if param2 == 0 else pos2

    if opcode == 99:
        print(data[0])
        break

    elif opcode == 1:
        # Adding operation
        data[pos3] = value1 + value2
        idx += 4

    elif opcode == 2:
        # Multiplication operation
        data[pos3] = value1 * value2
        idx += 4

    elif opcode == 3:
        # Input operation
        try:
            input_value = int(input("Provide Input: "))
            data[pos1] = input_value
            idx += 2
        except TypeError:
            print("Enter an integer!")
            break

    elif opcode == 4:
        # Ouput operation
        data[0] = value1
        idx += 2

    else:
        print(f"Unkonwn Operation: {operation}")
        break



print(data)