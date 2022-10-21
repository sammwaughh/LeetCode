# Plus One

# An integer is stored in an array with each digit in a different entry
# The most significiant digit is leftmost
# Add one to the integer and return the result as an array

def plusOne(digits):
    done = False
    i = len(digits)-1
    while not done:
        val = digits[i]
        if val != 9:
            digits[i] = val + 1
            done = True
        else:
            digits[i] = 0
            i -= 1
            if i == -1:
                digits = [1] + digits
                done = True
    return digits

print(plusOne([9]))
