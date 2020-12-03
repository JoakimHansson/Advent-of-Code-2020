import re

def countLetters(data):

    valid = 0

    for line in data:

        split = re.split('-| |: |\n',line)
        min = int(split[0])
        max = int(split[1])
        letter = split[2]
        password = split[3]
        count = password.count(letter)

        if min <= count and count <= max:
            valid += 1

    return valid

def checkPositions(data):

    valid = 0

    for line in data:
        split = re.split('-| |: |\n',line)
        pos1 = int(split[0]) -1
        pos2 = int(split[1]) -1
        letter = split[2]
        password = split[3]

        if password[pos1] == letter and password[pos2] != letter:
            valid += 1
        elif password[pos2] == letter and password[pos1] != letter:
            valid += 1

    return valid

if __name__ == '__main__':

    data = [line for line in open("data.txt", 'r')]

    valid_count = countLetters(data)
    valid_pos = checkPositions(data)

    print("part one: " + str(valid_count))
    print("part two: " + str(valid_pos))
