def main():
    
    #Preperatory dictionary declaration and output/report message.
    char_dict = {}
    char_list = []
    print("--- Begin Book Report of books/frankenstein.txt ---")
    
    #Open and read the text, define important variable for functions
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
        
        return char_dict


    ###resume work here:

    def sort_on(char_dict):
        return char_dict("char")
    
    def make_list(char_dict):
        

        return char_list
    


    count_words(file_contents)
    count_char(file_contents)
    print(char_list)

main()
