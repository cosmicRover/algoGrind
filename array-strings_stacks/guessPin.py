# O(n) time and space O(1)

def guessPin(pin, guess):

    left = 0
    right = len(guess) -1
    returnArray = ["-", "-", "-", "-"]

    while left < right:
        if guess[left] == pin[left]:
            returnArray[left] = "*"
        elif guess[left] in pin:
            returnArray[left] = "o"

        if guess[right] == pin[right]:
            returnArray[right] = "*"
        elif guess[right] in pin:
            returnArray[right] = "o"

        left += 1
        right -= 1
    return str("%s%s%s%s"  %(returnArray[0],returnArray[1],returnArray[2],returnArray[3]))


print(guessPin("1244", "6626"))
        