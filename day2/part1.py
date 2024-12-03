f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

safe = 0
for reading in input:
    val = reading.strip()
    values = [int(x) for x in val.split(" ")]
    is_safe = True
    is_increasing= values[0] - values[-1] < 0
    for i in range(1, len(values)):
        if values[i-1] == values[i]:
            is_safe = False
            break
        result = values[i-1] - values[i]
        if is_increasing:
            if result < -3 or result > 0:
                is_safe = False
                break
        else:
            if result > 3 or result < 0:
                is_safe = False
                break

    if is_safe:
        safe += 1
    

print(safe)
