def Hmap(pattern, s):
    # Split the string 's' into a list of words
    words = s.split()

    # If the length of the pattern doesn't match the number of words, return False
    if len(pattern) != len(words):
        return False

    # Create dictionaries to store the mappings from pattern characters to words and vice versa
    patternToWord = {}
    wordToPattern = {}

    # Iterate through each character in the pattern and the corresponding word in the list
    for char, word in zip(pattern, words):
        # If the character has been mapped to a different word, return False
        if char in patternToWord and patternToWord[char] != word:
            return False
        # If the word has been mapped to a different character, return False
        if word in wordToPattern and wordToPattern[word] != char:
            return False

        # Map the current character to the word and vice versa
        patternToWord[char] = word
        wordToPattern[word] = char

    # If no mismatches are found, return True
    return True

# Check if the script is being executed directly
if __name__ == "__main__":
    
    print(Hmap("cricket"," babar virat maxwell babar warner rizwan head"))
    print(Hmap("abcd", "ronaldo messi babar neymar"))
    print(Hmap("cket", "babar warner rizwan virat")) 