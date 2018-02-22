import numpy as np

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
            "short straight": {"value": 0, "scored": False},
            "long straight": {"value": 0, "scored": False},
            "chance": {"value": 0, "scored": False},
            "yahtzee": {"value": 0, "scored": False},
        }
        self.held = []
        self.pot = []

    def roll(self):
        return np.random.randint(1, 6, size=5 - len(self.held)).tolist()

    def get_score(self, cate):
        score = 0

        # Count number of each value on a 6-sided die
        tally = [0] * 6
        for die in self.pot:
            tally[die-1] += 1

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
        elif cate == "3 of a kind": # Three of a kind, score = sum of all dice
            three = False
            for i in range(len(tally)):
                if tally[i] >= 3:
                    three = True
                score += (i + 1) * tally[i]
            if not three: 
                score = 0 
        elif cate == "4 of a kind": # Four of kind, score = sum of all dice
            four = True
            for i in range(len(tally)):
                if tally[i] >= 4:
                    four = True
                score += (i + 1) * tally[i]
            if not four:
                score = 0
        elif cate == "chance": # No requirements, score = sum of all dice
            for die in self.pot:
                score += die
        elif cate == "full house": # A pair and a triplet, score = 25
            pair = False
            triplet = False
            for i in tally:
                if i == 2:
                    pair = True
                if i == 3:
                    triplet = True
            if pair and triplet:
                score = 25
        elif cate == "short straight" or cate == "long straight":
            best = 0
            consecutive = 0
            for i in tally:
                if i > 0:
                    consecutive += 1
                    if consecutive > best:
                        best = consecutive
                else:
                    consecutive = 0

            if cate == "short straight" and best >= 4: # straight of 4, score = 30
                score = 30
            elif cate == "long straight" and best >= 5: # straight of 5, score = 40
                score = 40
        elif cate == "yahtzee": # 5 of a kind, score = 50
            for i in tally:
                if i == 5:
                    score = 50
                        
        return score

    def update_score(self, cate, score):
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
        
        return True