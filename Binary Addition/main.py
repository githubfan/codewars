def add_binary(a,b):
    binary = bin(a+b)
    binary = str(binary)
    binary = binary.replace("0b", "")
    return binary

