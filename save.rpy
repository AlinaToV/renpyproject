#менюшка для сейвов
scrren_esc_menu():
tag menu
modal true 
zorder 100
#можно подогнать анимки
  frame at fade_in:
        xalign 0.5
        yalign 0.5
        padding 40
        background Frame("#222C", 20, 20)

        vbox:
            spacing 20
            style_prefix "esc"

            textbutton "Продолжить" action Return()
            textbutton "Сохранить игру" action ShowMenu("save")
            textbutton "Загрузить игру" action ShowMenu("load")
            textbutton "Загрузить автосейв" action FileLoad("auto-1")
            textbutton "Настройки" action ShowMenu("preferences")
            textbutton "Выйти в главное меню" action MainMenu()
            textbutton "Выйти из игры" action Quit(confirm=True)
