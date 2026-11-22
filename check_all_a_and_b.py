def checkString(s: str) -> bool:
    for i in range(len(s)-1):
        if s[i] == 'b' and s[i+1] == 'a':
            return False
    return True

print(checkString("aaabbb"))  # Output: True
print(checkString("abab"))    # Output: False