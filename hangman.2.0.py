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
    secret_word_inlist=list(secret_word)
    word_completion_s='_'*len(secret_word)
    word_completion=list(word_completion_s)
    
    for s in range(len(letters_guessed)):
       temp=letters_guessed[s]
       indices=[i for i,letter in enumerate(secret_word_inlist) if letter==temp ]
       for index in indices:
           word_completion[index]=temp
    if '_' in word_completion:
       word_completion=word_completion.remove('_')
    if secret_word_inlist==word_completion:
        return True
    else:
        return False
    
    
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_inlist=list(secret_word)
    word=list('_'*len(secret_word))
    
    for s in range(len(letters_guessed)):
       temp=letters_guessed[s]
       indices=[i for i,letter in enumerate(secret_word_inlist) if letter==temp ]
       for index in indices:
           word[index]=temp
    word_s=''.join(word)  
    word_r=word_s.replace('_','_ ')
    return word_r  
    
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
        
    alpha='abcdefghijklmnopqrstuvwxyz'
    
    alpha_list=list(alpha)
    
    
    if len(letters_guessed)==0:
        return alpha
    else:
        for c in letters_guessed:
            alpha_list.remove(c)
        return ''.join(alpha_list)
    
            
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    

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
    print('Wellcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long')
    print('----------------')
    print('Available letters:abcdefghijklmnopqrstuvwxyz')
    letters_guessed=[]
    guessed=False
    tries=6
    error=3
    count=0
    while not guessed and tries >0:
        if error<0:
                   tries=tries-1
                   count=count-1
        print('You have',tries,'guesses left')
        print('-----------------------','\n')
        guess=input('Please guess a letter:').lower()
        flag=True
        a_flag=False
        b_flag=False
        flag_c=False
        if len(guess)==1 and guess.isalpha():
            if guess in letters_guessed:
                error=error-1
                a_flag=True
                
            if a_flag==False:
               letters_guessed.append(guess)
               count=count+1
               if guess not in secret_word:
                   if guess in 'aeiou':
                       tries=tries-2
                       
                   else:
                     tries=tries-1
                   count=count-1
                   flag=False
               
               if is_word_guessed(secret_word,letters_guessed)==True:
                   print('\nCongratulations you won')
                   Total_score=tries*count
                   print('Your total score for this game is:',Total_score)
                   flag_c=True
                   break
               
        else:
            error=error-1
            b_flag=True
        if flag==True:
            print('Good guess:',get_guessed_word(secret_word,letters_guessed))
        if flag==False:
            print('Oops! That letter is not in my word',get_guessed_word(secret_word,letters_guessed))
        if b_flag==True:
            print('Oops! That is not a valid letter.You have',error,'warnings',get_guessed_word(secret_word,letters_guessed))
        if a_flag==True:
            print("Oops! You've already guessed that letter.You now have",error,"warnings:",get_guessed_word(secret_word,letters_guessed))
        print('Available letters:',get_available_letters(letters_guessed))
    if flag_c==True:
        pass
    else:        
        print('\nSorry you ran out of guesses.The word was',secret_word)     
    

    
    # FILL IN YOUR CODE HERE AND DELETE "pass"




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word,wrong_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    count1=0
    for letter in other_word:
        if letter in wrong_guessed:
            return False
    for e in range(len(my_word)):
        if my_word[e] != '_':
            if my_word[e]==other_word[e]:
                   count1+=1
    
    my_word=my_word.replace('_','')

    if count1==len(my_word):
        return True
    else:
        return False
        
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
 

def show_possible_matches(my_word,wrong_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
              Keep in mind that in hangman when a letter is guessed, all the positions
              at which that letter occurs in the secret word are revealed.
              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
              that has already been revealed.

    '''
    possible_matches=''
    my_word=my_word.replace(' ','')
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #print(show_possible_matches('y_ u_ h_ u_ _y'))
    for y in wordlist:
        if len(y)==len(my_word):
            
            if match_with_gaps(my_word,y,wrong_guessed):
                possible_matches=possible_matches + y +','
    return possible_matches[0:len(possible_matches)-1] 


# FILL IN YOUR CODE HERE AND DELETE "pass"
# print(show_possible_matches('y_ u_ h_ u_ _y'))       
# print(show_possible_matches('a_ '))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Wellcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long')
    print('If want to know possible word matches Enter:*')
    print('\n ************************************************************* \n')
    letters_guessed=[]
    wrong_guessed=[]
    guessed=False
    tries=6
    error=3
    count=0
    while not guessed and tries >0:
        if error<0:
                   tries=tries-1
                   count=count-1
        print('-----------------------------------------------------------------------')     
        print('You have',tries,'guesses left')
        print('Available letters:',get_available_letters(letters_guessed))
        guess=input('Please guess a letter:').lower()
        flag=True
        a_flag=False
        b_flag=False
        flag_c=False
        flag_d=False
        if len(guess)==1 and guess.isalpha():
            if guess in letters_guessed:
                error=error-1
                a_flag=True
                
            if a_flag==False:
               letters_guessed.append(guess)
               count=count+1
               if guess not in secret_word:
                     if guess in 'aeiou':
                        tries=tries-2
                       
                     else:
                        count=count-1
                        tries=tries-1
                     flag=False
                     wrong_guessed.append(guess)
                     
               if is_word_guessed(secret_word,letters_guessed)==True:
                   print('\nCongratulations you won')
                   Total_score=tries*count
                   print('Your total score for this game is:',Total_score)
                   flag_c=True
                   break
        elif guess=='*':
            print('Possible word matches are:',show_possible_matches(get_guessed_word(secret_word,letters_guessed),wrong_guessed))
            flag_d=True
        else:
            error=error-1
            b_flag=True
        if flag==True and flag_d==False:
            print('Good guess:',get_guessed_word(secret_word,letters_guessed))
        if flag==False and flag_d==False:
            print('Oops! That letter is not in my word',get_guessed_word(secret_word,letters_guessed))
        if b_flag==True and flag_d==False:
            print('Oops! That is not a valid letter.You have',error,'warnings',get_guessed_word(secret_word,letters_guessed))
        if a_flag==True and flag_d==False:
            print("Oops! You've already guessed that letter.You now have",error,"warnings:",get_guessed_word(secret_word,letters_guessed))
        print('Available letters:',get_available_letters(letters_guessed))
    if flag_c==True:
        pass
    else:        
        print('\nSorry you ran out of guesses.The word was',secret_word)

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# # When you've completed your hangman_with_hint function, comment the two similar
# # lines above that were used to run the hangman function, and then uncomment
# # these two lines and run this file to test!
# # Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word) 
