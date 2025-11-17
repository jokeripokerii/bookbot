#Open the chosen text file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

#Counts the number of words in the whole Frankenstein
def get_num_words():
    teksti = get_book_text("books/frankenstein.txt")
    sanat = len(teksti.split())
    print(f"Found {sanat} total words")

#Creates a dictionary of how many of each symbol there is
def letter_calc():
    teksti = get_book_text("books/frankenstein.txt")
    letter_dic = {}
    for letter in teksti.lower():
        if letter not in letter_dic:
            letter_dic[letter] = 1
        else:
            letter_dic[letter] += 1
    return letter_dic

#Creates a new cleaned list of dictionaries
def setup(items):
    dic_list = []
    for i in items:
        if i.isalpha():
            new_dic = {"char": "", "num": 0}
            new_dic["char"] = i
            new_dic["num"] = items[i]
            dic_list.append(new_dic)
    return dic_list

#Required for sorting to work
def sort_on(esineet):
    return esineet["num"]

#Sorts the dictionaries by count and prints results
def kaunistus(kaunistettava):
    kaunistettava.sort(reverse = True, key=sort_on)
    for e in kaunistettava:
        char = e["char"]
        num = e["num"]
        print(f"{char}: {num}")



