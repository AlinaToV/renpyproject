init python:
    all_cards = ['A', 'B', 'C'] #перем карт

    ww = 3 #поля
    hh = 3

    max_c = 2 
    card_size = 80 #текстовый режим

    max_time = 0.2 #таймер

    wait = 0.4 #кд
 
    img_mode = True # режим картинок

    values_list = []
    temp = []
    for fn in renpy.list_files(): # перебор всех файлов в папке изображения
        if fn.startswith("images/card_") and fn.endswith((".png")):
            name = fn[12:-4] #имя карты из пути
            renpy.image("card " + name, fn)
            if name != "empty" and name != "back":
                temp.append(str(name))

    #проверка на картинки если не нашли меняем на текст
    if len(temp) > 1:
        all_cards = temp
    else:
        img_mode = False

    # функция инициализации игрового поля
    def cards_init():
        global values_list
        values_list = []
        while len(values_list) + max_c <= ww * hh: #генерация заполнения карт поля по вайл
            current_card = renpy.random.choice(all_cards)
            for i in range(0, max_c):
                values_list.append(current_card)
        renpy.random.shuffle(values_list) # перемешивание
        while len(values_list) < ww * hh: #добавление карт если их меньше
            values_list.append('empty')

# экран игры
screen memo_scr:
    # таймер    
    timer 1.0 action If (memo_timer > 1, SetVariable("memo_timer", memo_timer - 1), Jump("memo_game_lose") ) repeat True
    # поле
    grid ww hh:
        align (.5, .5) # в центре
        for card in cards_list:
            button:
                left_padding 0
                right_padding 0
                top_padding 0
                bottom_padding 0
                background None
                if card["c_value"] == 'empty':
                    if img_mode:
                        add "card empty"
                    else:
                        text " " size card_size
                else:
                    if card["c_chosen"]:
                        if img_mode:
                            add "card " + card["c_value"]
                        else:
                            text card["c_value"] size card_size
                    else:
                        if img_mode:
                            add "card back"
                        else:
                            text "X" size card_size
                # нажатие на кнопку
                action If ( (card["c_chosen"] or not can_click), None, [SetDict(cards_list[card["c_number"]], "c_chosen", True), Return(card["c_number"]) ] )
    text str(memo_timer) xalign .5 yalign 0.0 size card_size

# сама игра
label brainhack:
    $ cards_init()
    $ cards_list = []
    python:
        for i in range (0, len(values_list) ):
            if values_list[i] == 'empty':
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":True} )   
            else:
                cards_list.append ( {"c_number":i, "c_value": values_list[i], "c_chosen":False} )   
    $ memo_timer = max_time

    show screen memo_scr

    label game_loop:
        $ can_click = True
        $ turned_cards_numbers = []
        $ turned_cards_values = []
        $ turns_left = max_c
        label turns_loop:
            if turns_left > 0:
                $ result = ui.interact()
                $ memo_timer = memo_timer
                $ turned_cards_numbers.append (cards_list[result]["c_number"])
                $ turned_cards_values.append (cards_list[result]["c_value"])
                $ turns_left -= 1
                jump turns_loop
        # - лишние карты при нажатии
        $ can_click = False
        if turned_cards_values.count(turned_cards_values[0]) != len(turned_cards_values):
            $ renpy.pause (wait, hard = True)
            python:
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_chosen"] = False
        else:
            $ renpy.pause (wait, hard = True)
            python: 
                for i in range (0, len(turned_cards_numbers) ):
                    cards_list[turned_cards_numbers[i]]["c_value"] = 'empty'
                for j in cards_list:
                    if j["c_chosen"] == False:
                        renpy.jump ("game_loop")
                renpy.jump ("game_win")
        jump game_loop

label game_lose:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    centered "{size=36}Потрачено{/size}"
    jump brainhack

label game_win:
    hide screen memo_scr
    $ renpy.pause (0.1, hard = True)
    centered "{size=36}{b}Легко{/b}{/size}"
    jump nex