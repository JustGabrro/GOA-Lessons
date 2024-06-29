def vaporcode(s):
    return "  ".join(char for char in s.upper() if char != " ")