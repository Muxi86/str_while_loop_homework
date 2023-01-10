def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    i = 0
    while len(s)>i:
        if s[i].islower():
            k+=1
        i+=1
    return k
print(main("CodeschoolUz"))