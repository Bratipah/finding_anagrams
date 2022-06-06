# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word.lower()
    anagram.lower()
    if len(word) == len(anagram):
        count = 0
        for o in anagram:
            check = o in word
            if check:
                count = count + 1
            else:
                return False
                break
        if count == len(anagram):
            return True
        else:
            return False
    else:
        return False


answer1 = input("enter the word: ")
answer2 = input("enter the anagram: ")

print(find_anagram(answer1.strip().replace(" ", ""), answer2.strip().replace(" ", "")))
