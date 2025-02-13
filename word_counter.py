import string

def clean_text(text):
    """
    This function removes punctuation and converts the text to lowercase to ensure accurate word counting.
    """
    # Remove punctuation using Python's string.punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert the text to lowercase to make word counting case-insensitive
    text = text.lower()
    return text

def count_words(text):
    """
    This function counts the total number of words in the cleaned text.
    """
    cleaned_text = clean_text(text)
    # Split the text by spaces and return the number of words
    words = cleaned_text.split()
    return len(words), words

def count_word_frequency(words):
    """
    This function counts the frequency of each word in the list.
    """
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def display_word_count(total_words, word_frequency):
    """
    This function displays the total word count and the frequency of each word.
    """
    print(f"Total number of words: {total_words}")
    print("\nWord Frequency:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

def main():
    print("Welcome to the Word Counter Program!")
    print("This program will count the total number of words and show their frequency.\n")
    
    # Get the user input
    user_input = input("Please enter a sentence or paragraph: ").strip()

    # Handle empty input
    if not user_input:
        print("No text entered. Exiting the program.")
        return
    
    # Count the total number of words and their frequencies
    total_words, words = count_words(user_input)
    word_frequency = count_word_frequency(words)
    
    # Display the results
    display_word_count(total_words, word_frequency)

if __name__ == "__main__":
    main()
