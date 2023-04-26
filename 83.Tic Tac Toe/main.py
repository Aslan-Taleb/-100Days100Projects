from library import *


def main():
    print(welcome)
    while True:
        players = ['X', 'O']
        current_player = 0
        while True:
            show_game()
            the_input = input(f"\nWhere will we put {players[current_player]} ? : ")
            clear_screen()
            # Check for invalid input
            while not is_valid_input(the_input):
                print("Invalid input, please try again.")
                the_input = input(f"Where we put '{players[current_player]}' : ")
            update_game(the_input, players[current_player])
            draw_detector = test_draw()
            if test_win(players[current_player]):
                victory(players[current_player])
                break
            if draw_detector:
                victory(None)
                break
            current_player = (current_player + 1) % 2
        print(f"\n X: {scores['px_score']}   Draws: {scores['nul']}    O: {scores['po_score']} \n")
        play_again = input("Do you want to play again? (y/n)  ")
        while play_again.lower() not in ["y", "n"]:
            print("Invalid input, please try again.")
            play_again = input("Do you want to play again? (y/n)  ")
        if play_again.lower() == "n":
            break
        clear_screen()


main()
