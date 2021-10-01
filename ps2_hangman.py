# Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 2
# Hangman
# Name: Harlin Kaur
# Time spent: 4-5hrs
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
##    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
##    print("  ", len(wordlist), "words loaded.")
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
wordlist = load_words()

# your code begins here!
                
def hangman(): 
    secretword = choose_word(wordlist)
    print("Welcome to the game, Hangman!")
    print('I am thinking of a word that is' + str(len(secretword)) +' letters long.')
    guessedword = len(secretword) * 2
    guess = ''
    letters=[]
    while(letters !=0):
        print('-------------')
        print('You have '+ str(guessedword) +' guesses left.')
        print('Available letters:',''.join(letters))
        guess = str(input('Please guess a letter:')).lower()
        word = ''
        for char in secretword:
            if char in guess:
               word = word + char + ' '
            else:
                word = word + '- ' 
        print('')           
        if guess in secretword:
           print('Good guess:',word)
           if guess in letters:
              letters.remove(guess) 
           if word.replace(' ','') == secretword:
               return True    
        else:
            print('Oops! You have already guessed that letter:' ,word)
            if guess in letters:
                letters.remove(guess)
            guessedword = guessedword - 1
    print('you loose, word was',secretword)
       
if hangman():
    print("Congratulation, you won!")
