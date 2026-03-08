def caesarCipher(s, k):
    k = k % 26
    result = []
    for char in s:
        if char.islower():
            result.append(chr((ord(char) - ord('a') + k) % 26 + ord('a')))
        elif char.isupper():
            result.append(chr((ord(char) - ord('A') + k) % 26 + ord('A')))
        else:
            result.append(char)
    return "".join(result)
