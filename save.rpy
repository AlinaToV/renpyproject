screen esc_menu():
    tag menu
    modal True
    zorder 100

    add Solid("#0008") as overlay

    frame at fade_in:
        xalign 0.5
        yalign 0.5
        padding 40
        background Frame("#222C", 20, 20)

        vbox:
            spacing 20
            style_prefix "esc"

            textbutton "Продолжить" action Return()
            textbutton "Сохранить игру" action [Hide("esc_menu"), ShowMenu("save")]
            textbutton "Загрузить игру" action [Hide("esc_menu"), ShowMenu("load")]
            textbutton "Загрузить автосейв" action [Hide("esc_menu"), FileLoad(1)]
            textbutton "Настройки" action [Hide("esc_menu"), ShowMenu("preferences")]
            textbutton "Выйти в главное меню" action [Hide("esc_menu"), MainMenu()]
            textbutton "Выйти из игры" action Quit(confirm=True)

transform fade_in:
    alpha 0.0
    linear 0.3 alpha 1.0
