def palindrome(inp):
    rev = inp[::-1]
    if rev == inp:
        return True
    return False