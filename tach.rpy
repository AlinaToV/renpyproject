label clicker_game:
    $ click_count = 0
    $ time_limit = 7.0
    $ game_won = False
    $ timer_running = True

    show screen clicker_screen

    $ renpy.pause(time_limit)

    if not game_won:
        hide screen clicker_screen
        "Время вышло! Попробуй ещё раз."
        jump clicker_game  # перезапуск мини-игры

    return



screen clicker_screen():
    modal True
    zorder 100

    frame:
        align (0.5, 0.1)
        text "Клики: [click_count]/10" size 40 color "#FFFFFF"

    imagebutton:
        idle "click.png"
        hover "click.png"
        action Function(increase_click)
        align (0.5, 0.5)
        at clicker_shake


init python:
    def increase_click():
        global click_count, game_won, timer_running
        if timer_running:
            click_count += 1
            if click_count >= 10:
                game_won = True
                timer_running = False
                renpy.hide_screen("clicker_screen")
                renpy.jump("end_mini_game")  

transform clicker_shake:
    on click:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 0
