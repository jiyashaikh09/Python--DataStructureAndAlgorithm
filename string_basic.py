def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def word_frequency(s):
    words = s.split()
    return {word: words.count(word) for word in words}
``
