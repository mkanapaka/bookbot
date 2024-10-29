def main():
    with open('books/frankenstein.txt', 'r') as file:
        text = file.read()
        words = text.split()
        num_words = len(words)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"The book has {num_words} words.")
    
        letter_counts = {}
        for char in text.lower():
            if char.isalpha():
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1
    
        print("/nLetter frequency:")
        for letter, count in sorted(letter_counts.items()):
            print(f"Letter {letter} was used : {count} times")
    
main()  # Call the main function to run the program

