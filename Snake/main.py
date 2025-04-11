import random
import curses

Screen = curses.initscr()

curses.curs_set(0)

Screen_hieght, Screen_width = Screen.getmaxyx()

Window = curses.newwin(Screen_hieght, Screen_width, 0, 0)

Window.keypad(True)
Window.timeout(150)

Snk_x = Screen_width//4
Snk_y = Screen_hieght//2

Snake = [
    [Snk_y, Snk_x],
    [Snk_y, Snk_x+1],
    [Snk_y, Snk_x+2]
]

food = [Screen_hieght//2, Screen_width//2]
Window.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = Window.getch()

    if next_key == -1:
        key = key
    else:
        key = next_key

    if Snake[0][0] in [0, Screen_hieght] or Snake[0][1] in [0, Screen_width] or Snake[0] in Snake[1:]:
        curses.endwin()
        quit()

    new_head = Snake[0]
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    Snake.insert(0, new_head)

    if Snake[0] == food:
        food = None
        while food is None:
            new_food = [random.randint(1, Screen_hieght-1), random.randint(1, Screen_width-1)]
            if new_food not in Snake:
                food = new_food
            else:
                food = None
        Window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = Snake.pop()
        Window.addch(tail[0], tail[1], ' ')
    Window.addch(Snake[0][0], Snake[0][1], curses.ACS_CKBOARD)
