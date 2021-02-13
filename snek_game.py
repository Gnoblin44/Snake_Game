
import curses

# terminal setup
curses.initscr()
stdscr = curses.newwin(20, 60, 0, 0)                                            # y,x
stdscr.keypad(True)
curses.noecho()
curses.curs_set(0)
stdscr.border(0)
stdscr.nodelay(True)


# snek position n food
snake = [[-5, 7], [-4, 7], [-6, 7]]
food = [-10, 10]

# game code or game logic

score = 0

while True:
    event = stdscr.getch()

    # for p in snake:
    #     stdscr.addch(p[0], )

curses.endwin()
print(f"Your final score: {score}")


