f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]


def calc_is_safe(values, is_increasing):
    for i in range(1, len(values)):
        if values[i - 1] == values[i]:
            return False
        result = values[i - 1] - values[i]
        if is_increasing:
            if result < -3 or result > 0:
                return False
        else:
            if result > 3 or result < 0:
                return False

    return True


safe = 0
for reading in input:
    val = reading.strip()
    values = [int(x) for x in val.split(" ")]
    is_safe = True
    is_increasing = values[0] - values[-1] < 0
    is_safe = calc_is_safe(values, is_increasing)

    if not is_safe:
        any_safe = False
        for i in range(len(values)):
            new_values = values[:i] + values[i + 1 :]
            if calc_is_safe(new_values, is_increasing):
                is_safe = True
                break

    if is_safe:
        safe += 1


print(safe)
