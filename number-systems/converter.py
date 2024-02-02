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


def binToHex(input):
    binHex = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }

    numList = [int(x) for x in str(input)]
    numList.reverse()

    while len(numList) % 4 != 0:
        numList.append(0)
    numList.reverse()

    output = []

    count = 0
    nibble = []
    for number in numList:
        nibble.append(number)
        count += 1
        if count == 4:
            toConvert = "".join(map(str, nibble))
            output.append(binHex[toConvert])

            count = 0
            nibble = []

    return "".join(map(str, reversed(output)))


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
        return int("-" + s)


print(binToHex(101100))
