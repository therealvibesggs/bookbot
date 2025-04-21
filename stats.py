# counts words in a book
def get_book_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        split_file_contents = file_contents.split()
        count = 0
        for word in split_file_contents:
            count += 1
        return print(f"Found {count} total words")
    
# sort function
def format_key(item):
    return item[1]

# format function
def formatted_dict(new_char_dict):
    output_dict = {}
    for char, count in new_char_dict.items():
        if char.isalpha():
            output_dict[char] = count
    return sorted(output_dict.items(), key=format_key, reverse=True)
    
# counts characters in a book
def get_book_char(path_to_file):
    from collections import Counter
    
    with open(path_to_file) as f:
        
        # Pull characters from file
        # Lower case so we don't treat upper/lower of same char as differen
        file_contents = f.read()
        lower_case_contents = file_contents.lower()
        
        # Convert contents to list
        char_book = list(lower_case_contents)

        # Convert contents to set
        unique_char_in_book = set(lower_case_contents)
        
        # Count number of each character in book
        char_dict = {}
        
        for char in unique_char_in_book:
            char_dict[char] = char_book.count(char)
        
    for key, count in formatted_dict(char_dict):
        print(f"{key}: {count}")
    
