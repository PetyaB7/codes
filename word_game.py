from function import load_words, display_board, check_word


def main():
    words = load_words("words.txt")
    found_words = set()
    board = [
        ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y']
    ]


    while True:
        display_board(board)
        print("Found words:", found_words)

        guess = input("Input a word or 'end' for exit: ").strip().lower()

        if guess == 'end':
            break


        if check_word(guess, words, found_words):
            print("Congratulations! You find the word. ", guess)
        else:
            print("This word is not valid.")

    print("End of the game")

if __name__ == "__main__":
    main()
