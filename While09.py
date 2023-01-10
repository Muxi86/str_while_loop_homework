def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    while s!=0:
        k += s%10
        s//=10
    return k
print(main(987654))