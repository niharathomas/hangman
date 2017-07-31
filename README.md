# Hangman
## Using Python 3.4 and Flask

- Get random work: http://setgetgo.com/randomword/get.php?len=4 (game_word)
    - Player specifies length of word (word_length)
    - Player specifies number of allowed guesses(available_guesses)
- Input Validation:
    - Verify that input is an alphabet
    - Input has not already been entered
- Game logic:
    - Initialize unguessed_alphabets set (Set of ascii uppercase characters)
    - Given a word, keep track of the position for each alphabet in the word (player_guessed_word)
    - For each guess (guess):
        - Validate guess:
            - Is length of guess == 1?
            - Is valid input (is valid uppercase ASCII)
            - Is not already guessed (char in unguessed_alphabets)?
        - If guess in game_word:
            - Replace all positions in player_guessed_word with guess
        - Else if guess not in game_word:
            - Add guess to incorrect_guess_list
            - Decrement available_guesses
            - If available_guesses == 0:
                - Player loses
         - If solved:
            - Notify player of win
           else:
            - Display word and notify defeat
            
- Multiple images for man and noose
- Have user guess an alphabet