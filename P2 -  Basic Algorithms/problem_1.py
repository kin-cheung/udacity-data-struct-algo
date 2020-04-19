def better_guess(num, guess) :
    return (guess + (num/guess)) / 2

def close_enough(num, guess) :
    return abs(num - guess * guess) < 1

def test(num, guess) :
    if close_enough(num, guess) :
        return int(guess)
    return test(num,  better_guess(num, guess))

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return test(number, 1)

print(sqrt(9))
# 3
print(sqrt(0))
# 0
print(sqrt(1))
# 1
print(sqrt(16))
# 4
print(sqrt(27))
# 5
print(sqrt(13))
# 3
print(sqrt(1.5))
# 1
print(sqrt(9.1))
# 3
print(sqrt(120.9))
# 10