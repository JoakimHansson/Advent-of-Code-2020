import re
def getValue(line, field):
    return line.partition(field+":")[2].partition(" ")[0]

def passChecker(data):
    count = 0
    valid_pass = [False for i in range(7)]
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for line in data:

        if line == '':
            valid_pass = [False for i in range(7)]
            continue

        if "byr" in line:
            byr = int(getValue(line, "byr"))
            if 1920 <= byr and byr <= 2002:
                valid_pass[0] = True
        if "iyr" in line:
            iyr = int(getValue(line, "iyr"))
            if 2010 <= iyr and iyr <= 2020:
                valid_pass[1] = True
        if "eyr" in line:
            eyr = int(getValue(line, "eyr"))
            if 2020 <= eyr and eyr <= 2030:
                valid_pass[2] = True
        if "hgt" in line:
            hgt = getValue(line, "hgt")
            num = int(re.findall("\d+", hgt)[0])
            if "cm" in hgt and 150 <= num and num <= 193:
                valid_pass[3] = True
            elif "in" in hgt and 59 <= num and num <= 76:
                valid_pass[3] = True
        if "hcl" in line:
            hcl = getValue(line, "hcl")
            if hcl[0] == '#' and len(hcl) == 7:
                valid_pass[4] = True
        if "ecl" in line:
            ecl = getValue(line, "ecl")
            if ecl in eye_colors:
                valid_pass[5] = True
        if "pid" in line:
            pid = getValue(line, "pid")
            if len(pid) == 9 and pid.isdigit():
                print(pid)
                valid_pass[6] = True

        if False not in valid_pass:
            count += 1
            valid_pass = [False for i in range(7)]

    return count

if __name__ == '__main__':

    data = [line.rstrip() for line in open("data.txt", 'r')]
    part2 = passChecker(data)
    print("part two: " + str(part2))
