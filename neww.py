# palindrome

def is_palindrome(s):
    if s is None:
        return False
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
#explain the code line by line:1. `def is_palindrome(s):` - This line defines a function named `is_pal