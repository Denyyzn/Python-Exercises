# This is the explicit/step-by-step solution to the "005 - Maximum" problem
def maximum(a, b, c):
    # Start by assuming the first number is the biggest
    biggest = a

    # If the second number is bigger, update biggest
    if b > biggest:
        biggest = b

    # If the third number is bigger, update biggest again
    if c > biggest:
        biggest = c

    # Return the largest number found
    return biggest