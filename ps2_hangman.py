# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program


# your code begins here!



def find_occurance(word, guess):
    occ = ()
    for i in range(0, len(word)):
        if( word[i] == guess ):
            occ += (i,)
    return occ        

def  update_miss(word, guess, miss):
    if( word.find(guess) == -1 ):
        miss += (guess,)
    return miss


def update_word(word, guess, result):
    occ = find_occurance(word, guess)
    
    for i in occ:
        result[i] = guess
       
    return result    




print "Welcome to the game Hangman"
wordlist = load_words()
word = choose_word(wordlist)
print "I am thinking of a word that is ", len(word)," letters long"
no_of_guess = len(word) + 3
print "You have ", no_of_guess," guesses"
miss = ()
hit = ()
result=[]
for i in range(0, len(word), 1):
    result += '-'
               
print 'Random :' + word
for i in range(no_of_guess, 0, -1):
    guess = raw_input(" Guess   :")
    occ = find_occurance(word, guess)
    miss = update_miss(word, guess, miss)
    print " Misses  :", miss
    result = update_word(word, guess, result)
    print " Word  :", "".join(result)
    if( word == str(result) ):
        print " Yippe !!! "
        exit(0) 
    elif( i == 0 ):
        print " You are hanged "
        exit(0) 
    print 'You have ' + str(i-1) + ' guessess left'
    



