i = 0
j = 0
k = 0
while i < 5000000:
    while j < 5000000:
        while k < 5000000:
            assert i+j*k >= 0
            k += 1
        j += 1
    i += 1
