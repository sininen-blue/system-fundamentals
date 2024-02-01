# TODO make floating poitn work
def binToDecimal(input):
    isNegative = False

    if input < 0:
        isNegative = True

    input = abs(input)

    numList = [int(x) for x in str(input)]
    numLen = len(numList) - 1
    output = 0

    for number in numList:
        output += number * pow(2, numLen)
        numLen -= 1

    if isNegative is False:
        return output
    else:
        return -output


def decToBinary(input):
    output = []
    isNegative = False

    if input < 0:
        isNegative = True

    input = abs(input)
    while input > 0.0:
        output.append(input % 2)
        input = input // 2

    s = "".join(map(str, reversed(output)))

    if isNegative is False:
        return int(s)
    else:
        return int("-"+s)


print(binToDecimal(-100100))
