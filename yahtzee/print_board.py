from colorama import Fore, Back, Style, init

init()

# TOP_LEFT = '\U0000250F'
# TOP_RIGHT = '\U00002513'
# BOT_LEFT = '\U00002517'
# BOT_RIGHT = '\U0000251B'
# VERT_LEFT = '\U00002523'
# VERT_RIGHT = '\U0000252B'

# HORI = '\U00002501'
# VERT = '\U00002503'
# DOT = '\U000025CF'

TOP_ROW = "┏━━━━━━━┓"
BOT_ROW = "┗━━━━━━━┛"

ONE = [TOP_ROW,
       "┃       ┃",
       "┃   ●   ┃",
       "┃       ┃",
       BOT_ROW]

TWO = [TOP_ROW,
       "┃ ●     ┃",
       "┃       ┃",
       "┃     ● ┃",
       BOT_ROW]

THREE = [TOP_ROW,
         "┃ ●     ┃",
         "┃   ●   ┃",
         "┃     ● ┃",
         BOT_ROW]

FOUR = [TOP_ROW,
        "┃ ●   ● ┃",
        "┃       ┃",
        "┃ ●   ● ┃",
        BOT_ROW]

FIVE = [TOP_ROW,
        "┃ ●   ● ┃",
        "┃   ●   ┃",
        "┃ ●   ● ┃",
        BOT_ROW]

SIX = [TOP_ROW,
       "┃ ●   ● ┃",
       "┃ ●   ● ┃",
       "┃ ●   ● ┃",
       BOT_ROW]


def print_results(results, subtotal, total):
    col_width = 19
    print("%s%s%s" % (TOP_LEFT, ''.join(
        [HORI for i in range(col_width)]), TOP_RIGHT))
    for item in results:
        print("%s%*s%s" % (VERT, col_width, item, VERT))
        if item[:4] == "sixs":
            print("%s%s%s" % (VERT_LEFT, ''.join(
                [HORI for i in range(col_width)]), VERT_RIGHT))
            print("%s%*s%3d%s" % (VERT, col_width - 3, "Subtotal: ", subtotal, VERT))
            print("%s%s%s" % (VERT_LEFT, ''.join(
                [HORI for i in range(col_width)]), VERT_RIGHT))
    print("%s%s%s" % (VERT_LEFT, ''.join(
        [HORI for i in range(col_width)]), VERT_RIGHT))
    print("%s%*s%3d%s" % (VERT, col_width - 3, "Total Score: ", total, VERT))
    print("%s%s%s" % (BOT_LEFT, ''.join(
        [HORI for i in range(col_width)]), BOT_RIGHT))


def print_pot(pot):
    dice = [ONE, TWO, THREE, FOUR, FIVE, SIX]
    row = ""
    # print(Fore.BLACK, Back.WHITE)
    for i in range(5):
        for die in pot:
            row += dice[die - 1][i]
        print(row)
        row = ""
    # print(Style.RESET_ALL)
