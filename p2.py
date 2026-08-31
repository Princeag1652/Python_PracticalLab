import string

def word_frequency_analyzer(text):
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces and split into words
    words = text.lower().split()

    # Total number of words
    total_words = len(words)

    # Frequency table
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Find palindrome words
    palindromes = []

    for word in frequency:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)

    # Display report
    print("\n========== TEXT ANALYSIS REPORT ==========")
    print("Total words:", total_words)
    print("Distinct words:", len(frequency))

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(word, ":", count)

    print("\nPalindrome Words:")
    if len(palindromes) == 0:
        print("No palindromes found.")
    else:
        for word in palindromes:
            print(word)


# Multiline string input
text = """
Python programming is fun. 
"""

word_frequency_analyzer(text)