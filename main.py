def main():
    char_dict = {}

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def count_words(file_contents):
        words = file_contents.split()
        return print(f"There are {len(words)} words in this document.")


    def count_char(file_contents):
        lowered_file = file_contents.lower()

        for char in lowered_file:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        
        return print(char_dict)

    count_words(file_contents)
    count_char(file_contents)

main()
