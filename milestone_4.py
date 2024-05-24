
import random

class Hangman:
    """
     A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    num_lives: int
        The number of lives the player has
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    
    
    """


    def __init__(self, word_list: list[str], num_lives=5) -> None:
            # Initializing the attributes as indicated in the docstring
            self.num_lives = num_lives
            self.word = random.choice(word_list) 
            print(f"This is the word: {self.word}")
            self.word_guessed = ['_'] * len(self.word) # 
            self.num_letters = len(set(self.word))
            print(f"This is the current state of the users guessed word: {self.word_guessed}")
            self.list_of_guesses = []

    def __check_guess(self, guess) -> None: 
        """
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter, thus reducing the num_letters variable by 1.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        (' __ ' = private methods cannot be accessed directly from outside the class, but used within class/subclass)

        guess: str
            The letter to be checked

        """
        guess.lower() # converts capitals in word to lowercase
        if guess in self.word:
            print(f"Good guess!: {guess} is in secret word {self.word}")
            for char in range(len(self.word)): # guess (letter) Itirates over the index's with the length of the word
                if self.word[char] == guess:
                    self.word_guessed[char] = guess
            self.num_letters -=1
        else:
            print(f"Guess {guess} not is not in secret word {self.word}: ")   
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word,you have {self.num_lives} lives left.")
        print(self.word_guessed)
    
    def ask_letter(self):
        """

        Asks the user for a letter and checks two things:
        1. If the character is a single character and within the alphabet
        2. If the letter has already been tried and within the list of guesses
        3. Appends the letter into the list of guesses tried
        If it passes both checks, it calls the check_letter method.
        
        
        """

        while True:
            letter = input("Enter your letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character: ")
                break
            elif letter in self.list_of_guesses:
                print(f"{letter} has already been tried.")
                break
            else: 
                self.list_of_guesses.append(letter)
                self.__check_guess(letter)
                break
