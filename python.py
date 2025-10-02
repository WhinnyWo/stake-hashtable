def hash_table(key):
    return sum(ord(char) for char in key) % 10