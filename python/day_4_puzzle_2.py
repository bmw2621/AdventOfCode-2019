# Create range of possibilities list and empty list to hold all possibilities which pass tests
possibilities = [x for x in range(402328, 864247 + 1)]
cleaned = []

# Iterate through all possibilities and test each possibility
for possibility in possibilities:

    # Ensure there is a repeated number somewhere in the possibility
    # Could probably be done faster with regex
    contains_test = False
    for test in ['0','1','2','3','4','5','6','7','8','9']:
        if (test*2 in str(possibility)) and (test*3 not in str(possibility)):
            contains_test = True

    # Split possibility into array of integers
    split_possibility = [int(x) for x in str(possibility)]

    # Iterate through split list to ensure each digit is <= the following digit
    gtet_test = True
    for i in range(5):
        if split_possibility[i] > split_possibility[i+1]:
            gtet_test = False

    # If it passes both tests, add it to the list of cleaned possibilities
    if contains_test and gtet_test:
        cleaned.append(possibility)

print(cleaned)
print(len(cleaned))