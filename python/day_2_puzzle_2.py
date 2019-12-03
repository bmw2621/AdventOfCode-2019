import urllib.request

req = urllib.request.Request(url='https://adventofcode.com/2019/day/2/input')
req.add_header("Cookie", # SESSION COOKIE)
with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')

# Clean data
data.replace("\n","")
data = data.split(",")
data = [int(i) for i in data]


def testMutation(noun, verb):
    data_copy = data.copy()
    data_copy[1], data_copy[2] = (noun, verb)

    idx = 0

    while True:
        operation, pos1, pos2, write_pos = (data_copy[idx], data_copy[idx + 1], data_copy[idx + 2], data_copy[idx + 3])

        if operation == 99:
            break
        elif operation == 1:
            # Adding operation
            try:
                data_copy[write_pos] = data_copy[pos1] + data_copy[pos2]
            except IndexError:
                break
        elif operation == 2:
            # Multiplication operation
            try:
                data_copy[write_pos] = data_copy[pos1] * data_copy[pos2]
            except IndexError:
                break
        else:
            print(f"Unkonwn Operation: {operation}")
            break

        idx += 4

    return data_copy[0]

for i in range(100):
    for j in range(100):
        print(f"Testing: {i}, {j}")
        if testMutation(i,j) == 19690720:
            answer_i = i
            answer_j = j
            answer = f"Noun: {i}   Verb: {j}"

print(answer)
print((answer_i * 100) + answer_j)