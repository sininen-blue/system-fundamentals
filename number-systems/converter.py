def binToDecimal(input):
    isNegative = False
    if input < 0:
        input = abs(input)
        isNegative = True

    input = str(input).split(".")
    output = 0

    integer = input[0]
    intExp = len(integer) - 1
    for number in integer:
        output += int(number) * (2**intExp)
        intExp -= 1

    try:
        fraction = input[1]
        frcExp = -1
        for number in fraction:
            output += int(number) * (2**frcExp)
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
        output = "-" + output
    return output


def decToBinary(input):
    isNegative = False
    if input < 0:
        isNegative = True
        input = abs(input)

    input = str(input).split(".")
    output = ""

    integer = int(input[0])
    while integer // 2 != 0:
        output += str(integer % 2)
        integer = integer // 2
    output += str(integer % 2)
    output = output[::-1]  # reverses

    try:
        fraction = float("."+input[1])
        count = 0
        bits = 16

        output = str(output) + "."
        while fraction * 2 != 0 and count <= bits:
            count += 1

            fraction = fraction * 2
            if fraction > 1.0:
                fraction -= 1
                output += "1"
            else:
                output += "0"
    except IndexError:
        pass

    output = float(output)
    if isNegative:
        output *= -1
    return output


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
    output = ""
    isNegative = False
    if input < 0:
        isNegative = True
        input = abs(input)

    isFloat = False
    if isinstance(input, float):
        isFloat = True
        input = input * 16**8
    input = round(input)

    while input // 16 != 0:
        remainder = input % 16
        output = decHex[remainder] + output
        input = input // 16
    remainder = input % 16
    output = decHex[remainder] + output

    if isNegative:
        output = "-"+output
    if isFloat:
        outLen = len(output)
        output = output[:outLen-8] + "." + output[outLen-8:]
    return output


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

    input = input.upper()
    input = str(input).split(".")
    output = ""

    integer = input[0]
    for number in integer:
        output = output + hexbin[number]

    try:
        fraction = input[1]
        output = output + "."

        for number in fraction:
            output = output + hexbin[number]

    except IndexError:
        pass

    if isNegative:
        output = float(output) * -1

    return float(output)


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
    input = input.split(".")

    integer = input[0]
    intExp = len(integer) - 1
    for number in integer:
        output += hexbin[number] * pow(16, intExp)
        intExp -= 1

    try:
        fraction = input[1]
        frcExp = -1
        for number in fraction:
            output += hexbin[number] * pow(16, frcExp)
            frcExp -= 1
    except IndexError:
        pass

    if isNegative:
        output *= -1
    return output
