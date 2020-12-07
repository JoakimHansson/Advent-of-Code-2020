#!/usr/bin/env python3

def search(bags, done, goal, count):
    for b in bags:
        if b[0] not in done:
            if goal in b[1]:
                count[0] += 1
                done.add(b[0])
                search(bags, done, b[0], count)

def checkBag(bag, bags):
    content = bags[bag].split(", ")
    count= 0
    for c in content:
        b = c.split(" ")
        if "other" not in b:
            nbag = b[1] + " " + b[2]
            count += int(c[0]) + (int(c[0]) * checkBag(nbag, bags))

    return count
if __name__ == '__main__':
    data = [ line.rstrip() for line in open("data.txt", 'r')]
    b = {}
    done = set()
    bags = []
    for line in open("data.txt", 'r'):
        bag = line.rstrip().split(" bags contain ")
        bags.append(bag)
        b[bag[0]] = bag[1]

    count = [0]
    search(bags, done, "shiny gold", count)
    c = checkBag("shiny gold", b)
    print(count[0])
    print(c)
