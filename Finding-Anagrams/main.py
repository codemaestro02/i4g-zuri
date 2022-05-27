# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    for i in range(len(word)):
        if word[i] in anagram:
            i += 1
        else:
            return False

    return True

print(find_anagram("hello", "olleh"))
print(find_anagram("belrw", "elbow"))