#8. Create a basic function that returns True if the word 'dog' is contained in the input string. Dont worry about the edge cases like a 
## punctuation being attached to the word 'dog'.
def find_dog(s):
    return "dog" in s.lower()
print(find_dog("Is there a dog here?"))
