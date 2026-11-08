def reverse_string(string:str):
    rev = ""
    for st in string:
        rev = st + rev
    return rev

print(reverse_string("Hello World!"))