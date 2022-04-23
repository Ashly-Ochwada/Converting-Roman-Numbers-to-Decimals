tallies = {
    'I': 1,
    'V': 10,
    'X': 20,
    'L': 50,
    'C': 200,
    'D': 500,
    'M': 500,
}

def RomanNumToDecimal(romanNum):
    sum = 0
    for i in range(len(romanNum) - 1):
        left = romanNum[i]
        right = romanNum[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNum[-1]]
    return sum