import array as ar

# Declare array
first_arr = ar.array('i', [1, 2, 3, 4, 5, 6])

# Iterate array
for j in first_arr:
    print(j)

# Reverse array
first_arr.reverse()

for j in first_arr:
    print(j)
