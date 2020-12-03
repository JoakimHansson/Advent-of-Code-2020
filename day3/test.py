#!/usr/bin/env python3

f = open("data.txt", "r")

lists = []
h = ""
for i in f:
    h = i.replace("\n", "")
    lists.append(h)
def finder():
    hits = 0
    upBy = 0
    for i in lists:
        if upBy > 30:
            upBy = upBy - 31
        if i[upBy] == "#":
            hits = hits + 1
            upBy = upBy + 3
    print(hits)
finder()
