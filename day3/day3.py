def countTrees(data, right, down):

    index = 0
    count = 0
    for i in range(len(data)):
        if i % down != 0:
            continue

        if data[i][index] == '#':
            count += 1

        index = (index + right) % (len(data[i]))

    return count

if __name__ == '__main__':

    data = [line.rstrip() for line in open("data.txt", 'r')]

    part1 = countTrees(data, 3, 1)
    part2 = part1

    slopes = [(1,1), (5,1), (7,1), (1,2)]
    for slope in slopes:
        (r, d) = slope
        part2 *= countTrees(data, r, d)

    print("part one: " + str(part1))
    print("part two: " + str(part2))
