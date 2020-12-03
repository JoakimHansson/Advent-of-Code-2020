def twoSum(sum, numbers):
    for num1 in numbers:
        num2 = sum - num1
        if num2 in numbers:
            print("part one: " + str(num1 * num2))
            return True
    return False

def threeSum(sum, numbers):
    for num1 in numbers:
        s = set()
        current_sum = sum - num1
        for num2 in numbers:
            if (current_sum - num2) in s:
                print("part two: " + str(num1 * num2 * (current_sum - num2)))
                return True
            s.add(num2)
    print("No threesum exists for number: " + str(sum))
    return False

if __name__ == '__main__':

    # Dict of all numbers
    numbers = {int(line.strip()) for line in open("data.txt", 'r')}

    twoSum(2020, numbers)
    threeSum(2020, numbers)
