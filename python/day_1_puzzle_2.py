import urllib.request

def determine_fuel(mass):
    return (mass//3)-2

req = urllib.request.Request(url='https://adventofcode.com/2019/day/1/input')
req.add_header("Cookie", # SESSION COOKIE)
with urllib.request.urlopen(req) as f:
    data = f.read().decode('utf-8')

data = data.split("\n")
data = data[:-1]

sum_of_requirements = []
fuel_requirement = []

for line in data:
    mass = int(line)
    fuel_mass = determine_fuel(mass)
    sum_of_requirements.append(fuel_mass)

    while fuel_mass > 0:
        fuel_mass = determine_fuel(fuel_mass)
        if fuel_mass > 0:
            fuel_requirement.append(fuel_mass)
print(fuel_requirement)
print(sum(fuel_requirement))
print(sum_of_requirements)
print(sum(sum_of_requirements))
print()
print(sum(fuel_requirement) + sum(sum_of_requirements))




