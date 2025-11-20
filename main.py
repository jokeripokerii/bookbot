import sys
from stats import get_num_words
from stats import letter_calc
from stats import kaunistus
from stats import setup

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    #Prints out the prettied list
    kaunistus(setup(letter_calc()))
    print("============= END ===============")

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
