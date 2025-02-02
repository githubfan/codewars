# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples

def generate_hashtag(s):
    invalidString = False
    if s == "":
        return invalidString
    newOutput = s.split(" ")
    newString = "#"
    for word in newOutput:
        word = word.lower()
        if word != "":
            newString += word[0].upper() + word[1:]
    if len(newString) > 140:
        return invalidString
    return newString
