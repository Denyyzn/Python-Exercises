# This is the explicit/step-by-step solution to the "002 - Is Even" problem
def is_even_explicit(num):
    # Compute the remainder when dividing by 2
    remainder = num % 2

    # Determine if the number is even based on the remainder
    if remainder == 0:
        result = True
    else:
        result = False

    # Return the result
    return result

# Explanation:
# - remainder = num % 2 calculates what's left after dividing by 2.
# - If remainder is 0, the number is even, otherwise odd.
# - We store the boolean in `result` and return it to make the logic explicit.