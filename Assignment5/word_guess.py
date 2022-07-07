import random

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    starting_display = len(secret_word) * ("-")
    redisplay = ''
    tries_left = INITIAL_GUESSES
    while True:
        print(f'The word now looks like this: {starting_display}')
        print(f'You have {tries_left} guesses left')
        ask_for_letter = input('Type a single letter here, then press enter: ')
        for i in range(len(secret_word)):
            if ask_for_letter.upper() == secret_word[i]:
                starting_display = list(starting_display)
                starting_display[i] = ask_for_letter.upper()
                for x in starting_display:
                    redisplay += x
                starting_display = redisplay
                redisplay = ''

        if ask_for_letter.upper() in secret_word and len(ask_for_letter.upper()) == 1:
            print("That guess is correct")

        if len(ask_for_letter) >= 2 and ask_for_letter.upper() in secret_word:
            tries_left = tries_left
            print('Guess should only be a single character.')

        if ask_for_letter.upper() not in secret_word:
            tries_left -= 1
            print(f"There are no {ask_for_letter.upper()}'s in the word")

        if tries_left == 0:
            print(f"Sorry, you lost. The secret word was: {secret_word}")
            break

        if starting_display == secret_word:
            print(f"Congratulations, the word is: {secret_word}")
            break


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    file = open(LEXICON_FILE)
    word_list = []
    for line in file:
        line = line[:-1]
        word_list.append(line)
    index = random.randrange(len(word_list))
    word = word_list[index]
    return word


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


if __name__ == "__main__":
    main()
