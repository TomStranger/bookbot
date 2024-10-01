def main():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

    def count_words(file_contents):
        words = file_contents.split()
        return print(len(words))

    def count_char(words):
        lowered_words = words.lower()
        
    
    
    
    
    count_words(file_contents)

main()
