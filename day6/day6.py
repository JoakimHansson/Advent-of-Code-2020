#!/usr/bin/env python3
import string

def partOne(data):
    p1count = 0
    p2count = 0
    answers = {}
    c = 0
    for answer in data:
        if len(answer) == 0:
            for a in answers:
                if answers[a] == c:
                    p2count += 1
            answers = {}
            c = 0
            continue
        else:
            for a in answer:
                if a not in answers:
                    answers[a] = 1
                    p1count += 1
                else:
                    answers[a] += 1

        c += 1

    for a in answers:
        if answers[a] == c:
            p2count += 1

    return p1count, p2count
if __name__ == '__main__':
    data = [{q for q in line.rstrip()} for line in open("data.txt", 'r')]

    (p1,p2) = partOne(data)

    print(p1)
    print(p2)
