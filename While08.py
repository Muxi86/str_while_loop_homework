def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    while s!=0:
        x = s%10
        if x%2!=0:
            k+=1
        s//=10
    return k
print(main(1567534))