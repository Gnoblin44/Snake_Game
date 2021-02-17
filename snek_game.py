
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

snake = [(4, 10), (4, 11), (4, 12)]
food = [10, 30]

# game code or game logic

ESC = 27
key = curses.KEY_RIGHT

score = 0

while key != ESC:
    event = stdscr.getch()
    stdscr.addstr(0, 0, f'Score {str(score)}' + ' ')
    stdscr.timout()

    for i in snake:
        stdscr.addch(i[0], i[1], '*')

    stdscr.addch(food[0], food[1], '%')

curses.endwin()
print("Your final score: %s" % score)


