from inputs import *

# number_words = [("1", "one"), ("2", "two"), ("3", "three"), ("4", "four"), ("5", "five"), ("6","six"), ("7", "seven"), ("8", "eight"), ("9", "nine")]
# # number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# def is_match(buffer):
#     num_semi_matches = 0
#     is_matched = False
#     for number, word in number_words:
#         if buffer == word:
#             return number
#         elif word.startswith(buffer):
#             num_semi_matches += 1

#     return False if num_semi_matches > 0 else None


# def parse_string(string):
#     buffer = ""
#     for char in string:
#         buffer += char
#         is_matched = is_match(buffer)
#         if is_matched

def get_number(string: str):
    number = ""
    index = 0
    len_string = len(string)

    while index < len_string:
        char: str = string[index]

        if char.isdigit():
            number += char
        # One
        elif char == "o" and string[index:index + 3] == "one":
            number += "1"
            index += 2
            continue
        elif char == "t":
            # Two
            if string[index:index + 3] == "two":
                number += "2"
                index += 2
                continue
            # Three
            elif string[index:index + 5] == "three":
                number += "3"
                index += 4
                continue
        elif char == "f":
            # Four
            if string[index:index + 4] == "four":
                number += "4"
                index += 3
                continue
            # Five
            elif string[index:index + 4] == "five":
                number += "5"
                index += 3
                continue
        elif char == "s":
            # Six
            if string[index:index + 3] == "six":
                number += "6"
                index += 2
                continue
            # Seven
            elif string[index:index + 5] == "seven":
                number += "7"
                index += 4
                continue
        # Eight
        elif char == "e" and string[index:index + 5] == "eight":
            number += "8"
            index += 4
            continue
        # Nine
        elif char == "n" and string[index:index + 4] == "nine":
            number += "9"
            index += 3
            continue

        index += 1

    return int(number[0] + number[-1])

    formated_string = string
    for digit, word in number_words:
        formated_string = formated_string.replace(word, digit)

    first = ""
    last = ""
    for char in formated_string:
        if char.isdigit():
            if not first:
                first = char
            else:
                last = char

    print(string, "--", formated_string, "--", first + last if last else first + first)
    return int(first + last if last else first + first)

total = 0
for line in day_1.split("\n"):
    if line:
        total += get_number(line)
print(total)