# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(lst):
    for item in lst:
        if item == 0:
            lst.remove(item)
            lst.append(0)
    return lst
