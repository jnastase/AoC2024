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


score = 0
for i in range(len(left)):
    l_val = left[i]
    in_count = 0
    for j in range(len(right)):
        r_val = right[j]
        if l_val == r_val:
            in_count += 1
    
    score += (l_val * in_count)

print(score)
