def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s = ''
    for i in range(0,n):
        s += str(i)
    return s