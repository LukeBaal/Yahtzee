from colorama import Fore, Back, Style, init

init()

TOP_LEFT = '\U0000250F'
TOP_RIGHT = '\U00002513'
BOT_LEFT = '\U00002517'
BOT_RIGHT = '\U0000251B'
VERT_LEFT = '\U00002523'
VERT_RIGHT = '\U0000252B'

HORI = '\U00002501'
VERT = '\U00002503'
DOT = '\U000025CF'
TOP_ROW = "%s%s%s%s%s%s%s"%(TOP_LEFT, HORI, HORI, HORI, HORI, HORI, TOP_RIGHT)
BOT_ROW = "%s%s%s%s%s%s%s"%(BOT_LEFT, HORI, HORI, HORI, HORI, HORI, BOT_RIGHT)
LEFT_PAD = "%s " % VERT
RIGHT_PAD = " %s" % VERT

ONE = [TOP_ROW, "%s     %s" %(VERT, VERT), "%s  %s  %s" %(VERT, DOT, VERT), "%s     %s" %(VERT, VERT), BOT_ROW]
TWO = [TOP_ROW, "%s     %s" %(VERT, VERT), "%s  %s  %s" %(VERT, DOT, VERT), "%s     %s" %(VERT, VERT), BOT_ROW]
THREE = [TOP_ROW, "%s     %s" %(VERT, VERT), "%s  %s  %s" %(VERT, DOT, VERT), "%s     %s" %(VERT, VERT), BOT_ROW]
FOUR = [TOP_ROW, "%s     %s" %(VERT, VERT), "%s  %s  %s" %(VERT, DOT, VERT), "%s     %s" %(VERT, VERT), BOT_ROW]
FIVE = [TOP_ROW, "%s%s   %s%s" %(VERT, DOT, DOT, VERT), "%s  %s  %s" %(VERT, DOT, VERT), "%s%s   %s%s" %(VERT, DOT, DOT, VERT), BOT_ROW]
SIX = [TOP_ROW, "%s     %s" %(VERT, VERT), "%s  %s  %s" %(VERT, DOT, VERT), "%s     %s" %(VERT, VERT), BOT_ROW]


def print_results(results, total):
    col_width = 18
    print("%s%s%*sFinal Results%*s" %(Fore.BLACK, Back.WHITE, 3, '', 4, ''))
    print("%s%s%s" %(TOP_LEFT, ''.join([HORI for i in range(col_width)]), TOP_RIGHT))
    for item in results:
        print("%s%-*s%s" %(VERT, col_width, item, VERT))
    print("%s%s%s" %(VERT_LEFT, ''.join([HORI for i in range(col_width)]), VERT_RIGHT))
    print("%s%-*s%s" %(VERT, col_width, total, VERT))
    print("%s%s%s%s" %(BOT_LEFT, ''.join([HORI for i in range(col_width)]), BOT_RIGHT, Style.RESET_ALL))

def print_pot(pot):
    dice = [ONE, TWO, THREE, FOUR, FIVE, SIX]
    # die_width = 5
    # print("%s%s%s%s%s" %(Fore.BLACK, Back.WHITE, TOP_LEFT, [HORI for i in range(die_width)], TOP_RIGHT))
    row = ""
    for i in range(5):
        for die in pot:
            row += dice[die - 1][i]
        print(row)
        row = ""
    # print("%s%s%s%s" %(BOT_LEFT, [HORI for i in range(die_width)], BOT_RIGHT, Style.RESET_ALL))

# print_pot([1, 1, 1, 1, 5, 1])