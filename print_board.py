from colorama import Fore, Back, Style, init

init()

TOP_LEFT = '\U0000250F'
TOP_RIGHT = '\U00002513'
BOT_LEFT = '\U00002517'
BOT_RIGHT = '\U0000251B'
HORI = '\U00002501'
VERT = '\U00002503'
DOT = '\U000025CF'
TOP_ROW = [TOP_LEFT, HORI, HORI, HORI, HORI, HORI, TOP_RIGHT]
BOT_ROW = [BOT_LEFT, HORI, HORI, HORI, HORI, HORI, BOT_RIGHT]
LEFT_PAD = "%s " % VERT 
RIGHT_PAD = " %s" % VERT
ONE = [TOP_ROW,
            [LEFT_PAD," ", " ", " ", RIGHT_PAD],
            [LEFT_PAD, " ", DOT, " ", RIGHT_PAD],
            [LEFT_PAD, " ", " ", " ", RIGHT_PAD],
            BOT_ROW]
TWO = [TOP_ROW,
            [LEFT_PAD, DOT, " ", " ", RIGHT_PAD],
            [LEFT_PAD, " ", " ", " ", RIGHT_PAD],
            [LEFT_PAD, " ", " ", DOT, RIGHT_PAD],
            BOT_ROW]
THREE = [TOP_ROW,
            [LEFT_PAD, DOT, " ", " ", RIGHT_PAD],
            [LEFT_PAD, " ", DOT, " ", RIGHT_PAD],
            [LEFT_PAD, " ", " ", DOT, RIGHT_PAD],
            BOT_ROW]
FOUR = [TOP_ROW,
            [LEFT_PAD, DOT, " ", DOT, RIGHT_PAD],
            [LEFT_PAD, " ", " ", " ", RIGHT_PAD],
            [LEFT_PAD, DOT, " ", DOT, RIGHT_PAD],
            BOT_ROW]
FIVE = [TOP_ROW,
            [LEFT_PAD, DOT, " ", DOT, RIGHT_PAD],
            [LEFT_PAD, " ", DOT, " ", RIGHT_PAD],
            [LEFT_PAD, DOT, " ", DOT, RIGHT_PAD],
            BOT_ROW]
SIX = [TOP_ROW,
            [LEFT_PAD, DOT, " ", DOT, RIGHT_PAD],
            [LEFT_PAD, DOT, " ", DOT, RIGHT_PAD],
            [LEFT_PAD, DOT, " ", DOT, RIGHT_PAD],
            BOT_ROW]

def output():
        print("%s%s" %(Fore.BLACK, Back.WHITE))
        print("%s" %(Style.RESET_ALL))