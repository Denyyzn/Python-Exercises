# This is the explicit/step-by-step solution to the "004 - Absolute Value" problem
def absolute_value(num):
    # If the number is negative, invert its sign
    if num < 0:
        return -num

    # Otherwise, return the number unchanged
    return num