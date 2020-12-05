def findPos(code, i, min, max, upper, lower):
    diff = max - min
    if code[i] == lower:
        if diff == 2:
            return min
        else:
            return findPos(code, i+1, min, max - round(diff/2), upper, lower)
    elif code[i] == upper:
        if diff == 2:
            return max-1
        else:
            return findPos(code, i+1, min + round(diff/2), max, upper, lower)
    else:
        print("Invalid code....")
        return

if __name__ == '__main__':
    data = [line.rstrip() for line in open("data.txt", 'r')]
    max_id = -1
    min_id = -1
    my_id = -1
    ids = set()

    for code in data:
        row = findPos(code[:7], 0, 0, 128, 'B', 'F')
        col = findPos(code[7:], 0, 0, 8, 'R', 'L')
        id = row * 8 + col
        ids.add(id)
        if id > max_id:
            max_id = id
        if id < min_id or min_id == -1:
            min_id = id

    for id in range(min_id, max_id):
        if id not in ids:
            my_id = id

    print("part one: ", max_id)
    print("part two: ", my_id)
