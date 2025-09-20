# Code to count number of set bits...
# (i)Set bit mean nos of 1s
# (ii) offset bit mean nos of 0s

def count_bits(n):
    set_count = 0
    offset_count = 0
    
    while n > 0:
        if n & 1:   # check last bit
            set_count += 1
        else:
            offset_count += 1
        n >>= 1     # right shift
    
    return set_count, offset_count


# Example
num = 13
ones, zeros = count_bits(num)
print("Number:", num)
print("Set bits (1s):", ones)
print("Offset bits (0s):", zeros)
