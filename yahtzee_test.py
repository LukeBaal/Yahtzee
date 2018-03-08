import re
import sys

import pestcontrol
from yahtzee.game import Game


class NullDevice:
    """ Null class to redirect stderr to """

    def flush(self):
        pass

    def write(self, s):
        pass


class YahtzeeTest(pestcontrol.PestCase):
    def roll_test(self):
        """ Test roll command """
        game = Game()
        die = re.compile('[1-6]+')
        # New turn roll
        game.roll([1, 2, 3, 4, 5])
        actual = True
        if game.pot is not None:
            for result in game.pot:
                if not die.match(str(result)):
                    actual = False
        elif game.pot is not None or len(game.pot) != 5:
            actual = False

        self.assertTrue(actual, "New Round roll")

        # game.held = [0, 1, 2]
        game.roll([4, 5])
        actual = True

        # Check if results were returned
        if game.pot is not None:
            for result in game.pot:
                if not die.match(str(result)):
                    actual = False
        elif game.pot is None or len(game.pot) != 3:
            actual = False

        self.assertTrue(actual, "Roll returned 3 integers between 1 and 6")

    def score_test(self):
        """  Test score command """
        game = Game()

        # 3 2's = 6 pts
        game.pot = [1, 2, 2, 2, 4]
        self.assertEquals(game.get_score("twos"), 6, "3 2's score test")

        # 3 2's, 0 5's for 5's = 0 pts
        self.assertEquals(game.get_score("fives"), 0, "0 5's score test")

        # 3 of a kind
        self.assertEquals(game.get_score("3 of a kind"),
                          11, "3 of a kind test")
        game.pot = [1, 1, 3, 4, 4]
        self.assertEquals(game.get_score("3 of a kind"),
                          0, "Invalid 3 of a kind test")

        # 4 of a kind
        self.assertEquals(game.get_score("4 of a kind"),
                          0, "Invalid 4 of a kind test")
        game.pot = [3, 3, 3, 3, 1]
        self.assertEquals(game.get_score("4 of a kind"),
                          13, "4 of a kind test")

        # Full House
        self.assertEquals(game.get_score("full house"),
                          0, "Invalid full house test")
        game.pot = [5, 5, 6, 6, 6]
        self.assertEquals(game.get_score("full house"), 25, "Full house test")

        # Short straight
        self.assertEquals(game.get_score("small straight"),
                          0, "invalid small straight test")
        game.pot = [1, 3, 4, 5, 6]
        self.assertEquals(game.get_score("small straight"),
                          30, "valid small straight test")

        # Long straight
        self.assertEquals(game.get_score("large straight"),
                          0, "invalid large straight test")
        game.pot = [1, 2, 3, 4, 5]
        self.assertEquals(game.get_score("large straight"),
                          40, "valid large straight test")

        # Chance
        self.assertEquals(game.get_score("chance"), 15, "Chance test")

        # Yahtzee
        game.pot = [1, 1, 1, 1, 1]
        self.assertEquals(game.get_score("yahtzee"), 50, "yahtzee test")

        # Invalid yahtzee score counts as 0
        game.pot = [3, 3, 2, 4, 1]
        self.assertEquals(game.get_score("yahtzee"), 0,
                          "Invalid yahtzee score test")

    def update_score_test(self):
        game = Game()

        # First yahtzee
        score = 50
        cate = "yahtzee"
        self.assertTrue(game.update_score(cate, score),
                        "First yahtzee scored test")
        self.assertEquals(game.score[cate]["value"], score,
                          "Update yahtzee score test")

        # Second yahtzee
        self.assertTrue(game.update_score(cate, score),
                        "Second yahtzee scored test")
        self.assertEquals(game.score[cate]["value"],
                          150, "Second yahtzee score test")

        # Initial scoring of ones
        score = 3
        cate = "ones"
        self.assertTrue(game.update_score(cate, score),
                        "First ones scored test")
        self.assertEquals(game.score[cate]["value"],
                          score, "Update ones score test")

        # Attempt at scoring ones a second time
        score = 4
        prev_score = game.score[cate]["value"]
        self.assertFalse(game.update_score(cate, score),
                         "Second ones score attempt test")
        self.assertEquals(game.score[cate]["value"],
                          prev_score, "Second ones score test")

        # Attempt to score a yahtzee after scratching the first yahtzee (score of 0)
        game = Game()
        cate = "yahtzee"
        score = 0
        self.assertTrue(game.update_score(cate, score),
                        "Yahtzee scratch scored test")
        self.assertEquals(game.score[cate]["value"],
                          0, "Yahtzee scratch score test")

        # Attempt second yahtzee (should not be scored, despite valid)
        score = 50
        self.assertFalse(game.update_score(cate, score),
                         "Yahtzee scored attempt after scratch test")
        self.assertEquals(game.score[cate]["value"], 0,
                          "Yahtzee score after atempt after scratch test")

        # Bonus pts test
        self.assertEquals(game.score[cate]["value"], 0, "No bonus test")
        game.score["sixs"]["value"] = 30
        game.score["fives"]["value"] = 25
        self.assertTrue(game.update_score("fours", 20),
                        "Update fours for bonus test")
        cate = "bonus"
        self.assertEquals(game.score[cate]["value"], 35, "Bonus score test")

    def parse_input_test(self):
        game = Game()

        # Valid hold command
        text = "roll 1 2 4"
        self.assertEquals(game.parse_input(text), ("roll", [
            1, 2, 4]), "Valid roll command test")

        # Invalid hold command
        text = "roll full house"
        self.assertEquals(game.parse_input(text), (None, None),
                          "Invalid roll command test")

        # Valid score command
        text = "score full house"
        self.assertEquals(game.parse_input(text),
                          ("score", "full house"), "Valid score command test")

        # Invalid score command
        text = "score 1 2 4"
        self.assertEquals(game.parse_input(text), (None, None),
                          "Invalid score command test")

    def is_game_over_test(self):
        game = Game()

        # Not all categoried scored, game is not over
        self.assertFalse(game.is_game_over(), "Game is not over test")

        # Set scored bool of all categories to true
        for cate in game.score:
            game.score[cate]["scored"] = True

        # Game is now over
        self.assertTrue(game.is_game_over(), "Game is over test")


if __name__ == "__main__":
    # Redirect stderr to a null class to avoid printing error messages during unit testing
    original_stderr = sys.stderr
    sys.stderr = NullDevice()

    YahtzeeTest().main()
