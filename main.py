from yahtzee.game import Game
from yahtzee.print_board import print_results

if __name__ == "__main__":

    game = Game()

    # for cate in game.score:
    #     game.score[cate]["scored"] = True
    
    # game.score["ones"]["scored"] = False
    
    game.run_game()

    result, total = game.get_current_score()
    print_results(result, total)
