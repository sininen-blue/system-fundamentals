def binToDecimal(input):
    isNegative = False
    if input < 0:
        input = abs(input)
        isNegative = True

    input = str(input).split(".")
    output = 0

    integer = input[0]
    intExp = len(integer)-1
    for number in integer:
        output += int(number) * (2 ** intExp)
        intExp -= 1

    try:
        fraction = input[1]
        frcExp = -1
        for number in fraction:
            output += int(number) * (2 ** frcExp)
            frcExp -= 1
    except IndexError:
        pass

    if isNegative:
        output *= -1

    return output


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

    isNegative = False
    if input < 0:
        input = abs(input)
        isNegative = True

    input = str(input).split(".")
    output = ""

    integer = input[0]
    while len(integer) % 4 != 0:
        integer = "0" + integer

    count = 0
    buffer = ""
    for number in integer:
        buffer += number
        count += 1

        if count == 4:
            output += binHex[buffer]
            buffer = ""
            count = 0

    try:
        fraction = input[1]

        while len(fraction) % 4 != 0:
            fraction = fraction + "0"

        count = 0
        buffer = ""

        output += "."
        for number in fraction:
            buffer += number
            count += 1

            if count == 4:
                output += binHex[buffer]
                buffer = ""
                count = 0

    except IndexError:
        pass

    if isNegative:
        output = "-"+output
    return output


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


def decToHex(input):
    decHex = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }

    output = []
    isNegative = False

    if input < 0:
        isNegative = True

    input = abs(input)
    while input > 0.0:
        output.append(decHex[input % 16])
        input = input // 16

    s = "".join(map(str, reversed(output)))

    if isNegative is False:
        return s
    else:
        return "-" + s


def hexToBin(input):
    hexbin = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    isNegative = False

    if input[0] == "-":
        isNegative = True
        input = input[1:]

    output = ""
    input = input.upper()

    for number in input:
        output += hexbin[number]

    if isNegative is False:
        return int(output)
    else:
        return int(output) * -1


def hexToDec(input):
    hexbin = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }

    isNegative = False

    if input[0] == "-":
        isNegative = True
        input = input[1:]

    output = 0
    input = input.upper()

    numLen = len(input) - 1
    for number in input:
        output += hexbin[number] * pow(16, numLen)
        numLen -= 1

    if isNegative is False:
        return output
    else:
        return output * -1


