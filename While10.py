def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    while s!=0:
        x = s%10
        if x%2!=0:
            k += x
        s//10
    return k
print(main(589765))