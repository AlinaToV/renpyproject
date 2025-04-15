
screen middle_frame:
    tag menu
    window:
        style "default"
        align (0.5, 0.5)  
        has frame:
            background "#215d2f9a" 
            padding (30, 20) 
            xysize (960, 575)
 
        vbox:
            spacing 20 

            text "Палочка сидит в подворотне целый вечер, она выглядит серьёзно настроенной, настолько, что рядом проходящие палки кидают копейки к её ногам. Неплохая схема заработка на гроб, но не стоит говорить, что по её задумке лицо должно быть жалобным, а не инвалидоподобным. Наступает ночь.":
                color "#e8e8e8" 
                size 26
                line_spacing 6
                xalign 0.5    
                align (0.5, 0.5)

            textbutton "Далее" action Jump("next_label"):
                align (0.5, 0.5) 

screen custom_window(next_label):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        add "pic"
        frame:
            style "menu_frame"
            xalign 0.5
            vbox:
                spacing 10
                xalign 0.5
                yalign 0.5
           
                textbutton "Закрыть" action [Return(next_label)] xalign 0.5

screen custom_window2(next_label2):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        add "scrin"
        frame:
            style "menu_frame"
            xalign 0.5
            vbox:
                spacing 10
                xalign 0.5
                yalign 0.5
           
                textbutton "Закрыть" action [Return(next_label2)] xalign 0.5              

screen first_frame():
    tag menu
    window:
        style "default"
        align (0.5, 0.5)  
        has frame:
            background "#5d72666e" 
            padding (30, 20) 
            xysize (960, 575)
 
        vbox:
            spacing 20 

            text "Служба для палочек, ТОЛЬКО СЕГОДНЯ!\n\n Выплаты каждой палочке по 5-ти палколионам!!!\nСвободный доступ к оружию, защита палочек и гордость.\nЕсли вы хотите поступить к нам в спецназ звоните по номеру \n|934289...":
                color "#f5f5f5" 
                size 26
                line_spacing 7
                xalign 0.5    

            textbutton "Далее" action Jump("first"):
                align (0.5, 0.5)   