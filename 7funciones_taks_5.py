def reverse_words(s):
    """Reverse the words in a string. Ignores trailing/extra whitespace."""
    return " ".join(s.split()[::-1])
