def load_words(filename):
    with open(filename, 'r') as file:
        return [word.strip().lower() for word in file]



def display_board(board):
    for row in board:
        print(' '.join(row))



def check_word(guess, words, found_words):
    if guess in words and guess not in found_words:
        found_words.add(guess)
        return True,False
