import imports

dictionary = imports.json.load(open("dictionary_alpha_arrays.json"))
da = imports.numpy.asarray(dictionary)

answer = 'y'

def get_meaning(word):
    if word in da[ord(word[0]) - ord('a')]:
        print(da[ord(word[0]) - ord('a')].get(word))
    else:
        close_matches = imports.difflib.get_close_matches(word, da[ord(word[0]) - ord('a')].keys(), n = 5)
        print("\nNo Such Word Found!!\nDid you mean : \n")
        for i in close_matches:
            print(i,sep = '\n')
        correct_word = input("\nEnter correct word : ")
        get_meaning(correct_word)
            



def get_word():
    print('\n')
    word = input("Search for meaning of word : ")
    word = word.lower()
    get_meaning(word)


while(answer == 'y'):
    get_word()
    answer = input("\nDo you want to search for another word? 'y' for yes, 'n' for no. : ")


