def main():
    import sys
    from stats import get_book_words
    from stats import get_book_char

    total_sys_args = len(sys.argv)
    
    if total_sys_args < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:        
        path_to_book = sys.argv[1]
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        
        print("----------- Word Count ----------")
        get_book_words(path_to_book)
        
        print("--------- Character Count -------")
        get_book_char(path_to_book)
main()