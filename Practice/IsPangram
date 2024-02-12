# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any characters otherthan alphabets)
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ','').lower()
    for letter in alphabet:
        if letter not in str1:
            return False
    return True


print(f'Is the given string pangram ? {ispangram("The quick brown fox jumps over the Lazy dog")}')
print(f'Is the given string pangram ? {ispangram("The quick grown fox jumps over the Lazy dog")}')

def ispangram2(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(' ','').lower()
    return set(alphabet) == set(str1)

print(f'Is the given string pangram ? {ispangram2("The quick brown fox jumps over the Lazy dog")}')
print(f'Is the given string pangram ? {ispangram2("The quick grown fox jumps over the Lazy dog")}')
