from yahtzee.game import Game
from yahtzee.print_board import print_results

if __name__ == "__main__":
    # Init game
    game = Game()

    # Start Game
    game.run_game()

    # Get and print final results
    result, subtotal, total = game.get_current_score()
    print_results(result, subtotal, total)
