def to_camel_case(text):
    newTextString = ""
    text = text.replace("_", "-")
    text = text.split("-")
    iterator = 0
    for item in text:
        if iterator == 0:
            if item != item.upper():
                newTextString += item
                iterator = 1
            else:
                iterator = 1
                newTextString += item
        else:
            newTextString += item.capitalize()
            iterator = 1
    return newTextString

print(to_camel_case("A-B-C"))
