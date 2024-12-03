f = open("input.txt", "r")
lines = f.readlines()

input = [x for x in lines]

left = []
right = []
for reading in input:
    val = reading.strip()
    l_val, r_val = val.split("  ")
    left.append(int(l_val))
    right.append(int(r_val))

left.sort()
right.sort()

distance = 0
for i in range(len(right)):
    diff = abs(right[i] - left[i])
    distance += diff

print(distance)
