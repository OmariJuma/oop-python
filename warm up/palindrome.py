def palindrome(string):
    cleanStr= string.lower()
    startPtr = 0
    endPtr = len(cleanStr) - 1
    
    while startPtr < endPtr:
        if cleanStr[startPtr] != cleanStr[endPtr]:
            return False
        startPtr+=1
        endPtr -=1
    return True

#test cases
print(palindrome("madam"))
print(palindrome("Racecar"))
print(palindrome("Palindrome"))
            