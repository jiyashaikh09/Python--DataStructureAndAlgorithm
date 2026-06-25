def remove_char(s, char):
    return s.replace(char, "")

def check_substring(s, sub):
    return sub in s

def snake_to_pascal(s):
    return s.replace("_", " ").title().replace(" ", "")
``
