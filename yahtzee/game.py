import sys
from random import randint

from .print_board import print_pot, print_results


def eprint(*args, **kwargs):
    """Print to stderr"""
    print(*args, file=sys.stderr, **kwargs)


class Game:
    def __init__(self):
        self.score = {
            "ones": {"value": 0, "scored": False},
            "twos": {"value": 0, "scored": False},
            "threes": {"value": 0, "scored": False},
            "fours": {"value": 0, "scored": False},
            "fives": {"value": 0, "scored": False},
            "sixs": {"value": 0, "scored": False},
            "3 of a kind": {"value": 0, "scored": False},
            "4 of a kind": {"value": 0, "scored": False},
            "full house": {"value": 0, "scored": False},
            "small straight": {"value": 0, "scored": False},
            "large straight": {"value": 0, "scored": False},
            "chance": {"value": 0, "scored": False},
            "yahtzee": {"value": 0, "scored": False},
            "bonus": {"value": 0, "scored": False}
        }
        self.pot = [0] * 5
        self.roll_num = 1

    def new_round(self):
        """ Start a new round """
        self.roll_num = 1
        self.roll([1, 2, 3, 4, 5])

        # Ask user to hold or score
        cmd = None
        while cmd == None:
            print("Roll #%d" % self.roll_num)
            print_pot(self.pot)
            user_input = input("Enter a command: ")
            cmd, args = self.parse_input(user_input)
            # If on the third roll, don't accept a hold command
            # since user must score
            if self.roll_num == 3 and cmd == "roll":
                eprint("No rolls left, must score!\n")
                cmd = None
            elif cmd == "roll":
                # If command is roll, roll only the given dice
                if args:
                    self.roll(args)
                else:
                    self.roll([1, 2, 3, 4, 5])
                self.roll_num += 1
                cmd = None
            elif cmd == "score":
                # If command is score, determine score for category
                # defined by args. Then ask user for confirmation
                # If not confirmed, prompt for new command

                # If category has already been scored, can't score again, unless yahtzee
                if self.score[args]["scored"] and args != "yahtzee":
                    cmd = None
                    eprint("Already scored for %s" % args)
                    continue

                score = self.get_score(args)
                confirm = input("Score %d pts for %s? (Yes/no) " %
                                (self.get_score(args), args))
                if confirm == "Yes" or confirm == "y" or confirm == "yes" or confirm == "Y":
                    self.update_score(args, score)
                else:
                    cmd = None

    def parse_input(self, option):
        """ Parse user input """
        valid = False
        if option == "help":
            print("\nHelp:\
                   \nReroll (keep none): 'roll'\
                   \nHold: ex. 'roll 1 2 4', will roll dice 1, 2, and 4 \
                   \nScore: ex 'score full house', will show the score for a full house with current dice\
                   \npoints: print current results")

        else:
            cmd = option.split(" ")
            if cmd[0] == "score" or cmd[0] == "roll" or cmd[0] == "points":
                if cmd[0] == "score":
                    args = ' '.join(cmd[1:])
                    try:
                        if self.score[args]:
                            valid = True
                    except KeyError:
                        eprint("Invalid score category!\n")
                elif cmd[0] == "points":
                    result, subtotal, total = self.get_current_score()
                    print_results(result, subtotal, total)
                else:
                    if len(cmd) > 1:
                        args = cmd[1:]
                        for i in range(len(args)):
                            try:
                                args[i] = int(args[i])
                                if args[i] >= 1 and args[i] <= 6:
                                    valid = True
                                else:
                                    valid = False
                                    eprint(
                                        "Must use numbers between 1 and 6 to definer which dice to roll!\n")
                            except ValueError:
                                eprint(
                                    "Must use numbers between 1 and 6 to define which dice to roll!\n")
                    else:
                        args = None
                        valid = True
        if valid:
            return cmd[0], args
        else:
            return None, None

    def roll(self, to_roll):
        # Roll the dice at the given indexs
        for index in to_roll:
            self.pot[index - 1] = randint(1, 6)

    def get_score(self, cate):
        """ Calculate the score for the given category, with the current dice"""
        score = 0

        # If category is already scored, ignore it (except for yahtzees)
        if self.score[cate]["scored"] and cate != "yahtzee":
            return 0

        # Count number of each value on a 6-sided die
        tally = [0] * 6
        for die in self.pot:
            tally[die - 1] += 1

        # For number categories, score = sum of matching number (ie. 3 2's for twos = 6 pts)
        if cate == "ones":
            score = tally[0]
        elif cate == "twos":
            score = tally[1] * 2
        elif cate == "threes":
            score = tally[2] * 3
        elif cate == "fours":
            score = tally[3] * 4
        elif cate == "fives":
            score = tally[4] * 5
        elif cate == "sixs":
            score = tally[5] * 6
        elif cate == "3 of a kind":  # Three of a kind, score = sum of all dice
            three = False
            for i in range(len(tally)):
                if tally[i] >= 3:
                    three = True
                score += (i + 1) * tally[i]
            if not three:
                score = 0
        elif cate == "4 of a kind":  # Four of kind, score = sum of all dice
            four = False
            for i in range(len(tally)):
                if tally[i] >= 4:
                    four = True
                score += (i + 1) * tally[i]
            if not four:
                score = 0
        elif cate == "chance":  # No requirements, score = sum of all dice
            for die in self.pot:
                score += die
        elif cate == "full house":  # A pair and a triplet, score = 25
            pair = False
            triplet = False
            for i in tally:
                if i == 2:
                    pair = True
                if i == 3:
                    triplet = True
            if pair and triplet:
                score = 25
        elif cate == "small straight" or cate == "large straight":
            best = 0
            consecutive = 0
            for count in tally:
                if count > 0:
                    consecutive += 1
                    if consecutive > best:
                        best = consecutive
                else:
                    consecutive = 0

            if cate == "small straight" and best >= 4:  # straight of 4, score = 30
                score = 30
            elif cate == "large straight" and best >= 5:  # straight of 5, score = 40
                score = 40
        elif cate == "yahtzee":  # 5 of a kind, score = 50
            for i in tally:
                if i == 5:
                    if not self.score[cate]["scored"]:
                        score = 50
                    else:
                        score = 100

        return score

    def update_score(self, cate, score):
        """ Update the score of the given category """
        # Only yahtzees can be score multiple times
        if self.score[cate]["scored"]:
            # Additional yahtzees are worth 100 pts (if first yahtzee was valid)
            if cate == "yahtzee" and self.score["yahtzee"]["value"] > 0:
                self.score[cate]["value"] += 100
            else:
                return False
        else:
            self.score[cate]["value"] = score
            self.score[cate]["scored"] = True

            # If the total of the number categories is 63 or more, get 35 bonus pts
            if not self.score["bonus"]["scored"]:
                if cate == "ones" or cate == "twos" or cate == "threes" or cate == "fours" or cate == "fives" or cate == "sixs":
                    subtotal = 0
                    subtotal += self.score["ones"]["value"]
                    subtotal += self.score["twos"]["value"]
                    subtotal += self.score["threes"]["value"]
                    subtotal += self.score["fours"]["value"]
                    subtotal += self.score["fives"]["value"]
                    subtotal += self.score["sixs"]["value"]
                    if subtotal > 63:
                        self.score["bonus"]["value"] = 35
                        self.score["bonus"]["scored"] = True

        return True

    def is_game_over(self):
        """ Check if game is over (all categories have been scored) """
        for cate in self.score:
            if not self.score[cate]["scored"] and cate != "bonus":
                return False
        return True

    def get_current_score(self):
        """ Log Category score, calculate subtotal and total scores """
        subtotal = 0
        total = 0
        result = []
        for cate in self.score:
            total += self.score[cate]["value"]
            if cate == "sixs":
                subtotal = total
            result.append("%s: %2d" % (cate, self.score[cate]["value"]))
        return result, subtotal, total

    def run_game(self):
        """ Print help screen and keep starting a new round until game is over """
        print("\nHelp:\
                   \nReroll (keep none): 'roll'\
                   \nHold: ex. 'roll 1 2 4', will roll dice 1, 2, and 4 \
                   \nScore: ex 'score full house', will show the score for a full house with current dice\
                   \npoints: print current results")
        while not self.is_game_over():
            self.new_round()
