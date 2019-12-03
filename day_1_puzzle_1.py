import urllib.request

req = urllib.request.Request(url='https://adventofcode.com/2019/day/1/input')
req.add_header("Cookie", #SESSION COOKIE)
with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')

data = data.split("\n")
data = data[:-1]

sum_of_requirements = 0

for line in data:
    mass = int(line)
    sum_of_requirements += (mass//3)-2

print(sum_of_requirements)