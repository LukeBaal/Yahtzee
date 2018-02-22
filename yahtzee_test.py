import re

import numpy as np

from PyTest.pest_control import Pest
from yahtzee import Game


def roll_test(p):
    game = Game()
    die = re.compile('[1-6]+')
    # New turn roll
    results = game.roll()
    actual = True
    if results is not None:
        for result in results:
            if not die.match(str(result)):
                actual = False
    elif results is not None or len(results) != 5:
        actual = False

    p.assertTrue(actual, "New Round roll")

    game.held = [1, 1, 5]
    results = game.roll()
    actual = True

    # Check if results were returned
    if results is not None:
        for result in results:
            if not die.match(str(result)):
                actual = False
    elif results is None or len(results) != 3:
        actual = False

    p.assertTrue(actual, "Roll returned 3 integers between 1 and 6")

def score_test(p):
    game = Game()

    # 3 2's = 6 pts
    game.pot = [1, 2, 2, 2, 4]
    p.assertEquals(game.get_score("twos"), 6, "3 2's score test")

    # 3 2's, 0 5's for 5's = 0 pts
    p.assertEquals(game.get_score("fives"), 0, "0 5's score test")

    # 3 of a kind
    p.assertEquals(game.get_score("3 of a kind"), 11, "3 of a kind test")

    # 4 of a kind
    game.pot = [3, 3, 3, 3, 1]
    p.assertEquals(game.get_score("4 of a kind"), 13, "4 of a kind test")

    # Full House
    game.pot = [5, 5, 6, 6, 6]
    p.assertEquals(game.get_score("full house"), 25, "Full house test")

    # Short straight
    p.assertEquals(game.get_score("short straight"), 0, "invalid short straight test")
    game.pot = [1, 3, 4, 5, 6]
    p.assertEquals(game.get_score("short straight"), 30, "valid short straight test")
    
    # Long straight
    p.assertEquals(game.get_score("long straight"), 0, "invalid long straight test")
    game.pot = [1, 2, 3, 4, 5]
    p.assertEquals(game.get_score("long straight"), 40, "valid long straight test")

    # Chance
    p.assertEquals(game.get_score("chance"), 15, "Chance test")

    # Yahtzee
    game.pot = [1, 1, 1, 1, 1]
    p.assertEquals(game.get_score("yahtzee"), 50, "yahtzee test")

    # Invalid yahtzee score counts as 0
    game.pot = [3, 3, 2, 4, 1]
    p.assertEquals(game.get_score("yahtzee"), 0, "Invalid yahtzee score test")


def update_score_test(p):
    game = Game()

    # First yahtzee
    score = 50
    cate = "yahtzee"
    p.assertTrue(game.update_score(cate, score), "First yahtzee scored test")
    p.assertEquals(game.score[cate]["value"], score, "Update yahtzee score test")

    # Second yahtzee
    p.assertTrue(game.update_score(cate, score), "Second yahtzee scored test")
    p.assertEquals(game.score[cate]["value"], 150, "Second yahtzee score test")

    # Initial scoring of ones
    score = 3
    cate = "ones"
    p.assertTrue(game.update_score(cate, score), "First ones scored test")
    p.assertEquals(game.score[cate]["value"], score, "Update ones score test")

    # Attempt at scoring ones a second time
    score = 4
    prev_score = game.score[cate]["value"]
    p.assertFalse(game.update_score(cate, score), "Second ones score attempt test")
    p.assertEquals(game.score[cate]["value"], prev_score, "Second ones score test")

    # Attempt to score a yahtzee after scratching the first yahtzee (score of 0)
    game = Game()
    cate = "yahtzee"
    score = 0
    p.assertTrue(game.update_score(cate, score), "Yahtzee scratch scored test")
    p.assertEquals(game.score[cate]["value"], 0, "Yahtzee scratch score test")

    # Attempt second yahtzee (should not be scored, despite valid)
    score = 50
    p.assertFalse(game.update_score(cate, score), "Yahtzee scored attempt after scratch test")
    p.assertEquals(game.score[cate]["value"], 0, "Yahtzee score after atempt after scratch test")


if __name__ == "__main__":
    p = Pest()

    roll_test(p)
    score_test(p)
    update_score_test(p)

    p.run()
