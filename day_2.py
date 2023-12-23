from inputs import day_2

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def part_1():
    total = 0
    for game in day_2.split("\n"):
        if not game:
            continue

        possible = True

        sets = game.split(":")[1].split(";")
        for set in sets:
            for color in set.split(","):
                if int(color.split()[0]) > limits[color.split()[1]]:
                    possible = False
                    break

            if not possible:
                break

        if possible:
            total += int(game.split(":")[0].split()[1])

    print(total)

def part_2():
    total = 0
    for game in day_2.split("\n"):
        if not game:
            continue

        colors_max = {"red": 0, "green": 0, "blue": 0}
        sets = game.split(": ")[1].split("; ")
        for set in sets:
            for color in set.split(", "):
                color_name = color.split()[1]
                value = int(color.split()[0])

                if value > colors_max[color_name]:
                    colors_max[color_name] = value

        total += colors_max["red"] * colors_max["green"] * colors_max["blue"]

    print(total)

part_2()