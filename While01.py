def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    i = 0
    while i<len(s):
        if s[i].isdigit():
            k+=1
        i+=1
    return k

print(main("python 2022"))