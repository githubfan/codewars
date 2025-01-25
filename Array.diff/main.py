def array_diff(a, b):
    removalList = []
    for item in a:
        if item in b:
            removalList.append(item)
    for item in removalList:
        a.remove(item)
    return a
