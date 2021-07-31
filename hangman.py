# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    li = letters_guessed
    lis = list(secret_word)
    for letter in lis:
      if letter not in li:
        return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    li = letters_guessed
    lis = list(secret_word)
    outword = list("_" * len(lis))
    resultant = ""
    for letter in li:
      for index in range(len(lis)):
        if letter == lis[index]:
          outword[index] = letter
    for ele in outword:
      resultant += ele
      resultant += " "
    return resultant




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    unlisted = list(string.ascii_lowercase)
    li = letters_guessed
    lis = ""
    for letter in li:
      for chara in unlisted:
        if chara == letter:
          unlisted.remove(chara)
    for ele in unlisted:
      lis += ele
    return lis
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    guesslist = []
    warnings = 3
    vowels = "aeiou"
    print(f"Welcome to hangman, your word has: {len(secret_word)} letters and you will have {guesses} guesses.")
    print(get_guessed_word(secret_word, guesslist))
    while guesses > 0:
      if guesses > 1:
        print(f"You have {guesses} guesses left.")
      else:
        print("You have 1 guess left.")
      takein = input("Type your guess as a letter: ").lower()
      check = takein.islower() and takein not in guesslist and len(takein) == 1
      while check == False:
        if warnings >= 0:
          print(f"\nYou typed an invalid input or duplicate letter. Amount of mistakes allowed left: {warnings}")
        else:
          print("\nNo more warnings.")
        warnings -= 1
        if warnings < 0:
          print("Too many warnings, you will lose a guess.")
          guesses -= 1
          print(f"You have {guesses} guesses left.")
          if guesses == 0:
            print("\nFuck you.")
            break
        takein = input("Type your guess as a letter: ")
        check = takein.islower() and takein not in guesslist and len(takein) == 1
      if guesses == 0:
        break
      guesslist.append(takein)
      if takein in secret_word:
        print(f"The letter {takein} is in the word.")
      if takein not in secret_word and takein not in vowels:
        print(f"The letter {takein} is not in the word. You lose 1 guess for the wrong consonant.")
        guesses -= 1
      if takein not in secret_word and takein in vowels:
        print(f"The letter {takein} is not in the word. You lose 2 guesses for the wrong vowel.")
        guesses -= 2
      print(f"Word: {get_guessed_word(secret_word, guesslist)}")
      print(f"Unused letters: {get_available_letters(guesslist)}.")
      print("\n ----------------------------------------------- \n")
      if is_word_guessed(secret_word, guesslist) == True:
        print(f"Congratulations! You have guessed the word: {secret_word}!")
        print(f"Your score is {guesses * len(secret_word)}.")
        guesses = 0
    if is_word_guessed(secret_word, guesslist) == False:
      print(f"You did not guess the word: {secret_word}, before Bob hung himself.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = 0
    if len(my_word) != len(other_word):
      return False
    for position in range(0,len(my_word)):
      if my_word[position] == other_word[position] or my_word[position] == '_':
        matches += 1
    if matches == len(my_word):
      return True
    else:
      return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist:
      condition = match_with_gaps(my_word, word)
      if condition == True:
        print(word)

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply oneguess per round. Make sure to check that the user guesses a letter
       
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    guesslist = []
    warnings = 3
    vowels = "aeiou"
    print(f"Welcome to hangman, your word has: {len(secret_word)} letters and you will have {guesses} guesses.")
    print(get_guessed_word(secret_word, guesslist))
    while guesses > 0:
      if guesses > 1:
        print(f"You have {guesses} guesses left.")
      else:
        print("You have 1 guess left.")
      takein = input("Type your guess as a letter: ").lower()
      check = takein.islower() and takein not in guesslist and len(takein) == 1 or takein == '*'
      if takein == '*':
        show_possible_matches((get_guessed_word(secret_word, guesslist)).replace(" ", ""))
      while check == False:
        if warnings >= 0:
          print(f"\nYou typed an invalid input or duplicate letter. Amount of mistakes allowed left: {warnings}")
        else:
          print("\nNo more warnings.")
        warnings -= 1
        if warnings < 0:
          print("Too many warnings, you will lose a guess.")
          guesses -= 1
          print(f"You have {guesses} guesses left.")
          if guesses == 0:
            print("\nFuck you.")
            break
        takein = input("Type your guess as a letter: ")
        check = takein.islower() and takein not in guesslist and len(takein) == 1 or takein == '*'
      if guesses == 0:
        break
      if takein != '*':
        guesslist.append(takein)
      if takein in secret_word:
        print(f"The letter {takein} is in the word.")
      if takein not in secret_word and takein not in vowels and takein != '*':
        print(f"The letter {takein} is not in the word. You lose 1 guess for the wrong consonant.")
        guesses -= 1
      if takein not in secret_word and takein in vowels and takein != '*':
        print(f"The letter {takein} is not in the word. You lose 2 guesses for the wrong vowel.")
        guesses -= 2
      print(f"Word: {get_guessed_word(secret_word, guesslist)}")
      print(f"Unused letters: {get_available_letters(guesslist)}.")
      print("\n ----------------------------------------------- \n")
      if is_word_guessed(secret_word, guesslist) == True:
        print(f"Congratulations! You have guessed the word: {secret_word}!")
        print(f"Your score is {guesses * len(secret_word)}.")
        guesses = 0
    if is_word_guessed(secret_word, guesslist) == False:
      print(f"You did not guess the word: {secret_word}, before Bob hung himself.")




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # secret_word = "apple"
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    # secret_word = "apple"
    hangman_with_hints(secret_word)
