screen custom_save_load_menu(mode="save"):

    modal True
    tag custom_menu

    frame:
        style "menu_frame"
        align (0.5, 0.5)
        padding (20,20)

        vbox:
            spacing 10

            text "Выберите слот:" size 30

            # Слот 1
            if mode == "save":
                textbutton "Слот 1" action Function(renpy.save, "custom_slot_1")
            else:
                textbutton "Слот 1" action Function(renpy.load, "custom_slot_1")

            # Слот 2
            if mode == "save":
                textbutton "Слот 2" action Function(renpy.save, "custom_slot_2")
            else:
                textbutton "Слот 2" action Function(renpy.load, "custom_slot_2")

            # Слот 3
            if mode == "save":
                textbutton "Слот 3" action Function(renpy.save, "custom_slot_3")
            else:
                textbutton "Слот 3" action Function(renpy.load, "custom_slot_3")
            
            textbutton "Отмена" action Hide("custom_save_load_menu")

