init python:
    import time
    start_time = time.time()
    inventory = {
        "timer": 1, 
        "lucky_coin": 1, 
    }
    def get_playtime():
        elapsed_time = time.time() - start_time  
        hours = int(elapsed_time // 3600) 
        minutes = int((elapsed_time % 3600) // 60) 
        seconds = int(elapsed_time % 60) 
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    can_give_coin = False  #активация для монетки НЕ ЗАБЫТЬ

    def give_lucky_coin():
        global inventory
        if inventory.get("lucky_coin", 0) > 0:
            inventory["lucky_coin"] -= 1
            return True
        return False

screen inventory_screen:
    tag menu
    window:
        style "menu_window"
        text "Инвентарь"
        
    vbox:
        text "Время в игре: [get_playtime()]"
        if inventory.get("timer", 0) > 0:
            hbox:
                image "timer.png"  
                text "Таймер активен."

        if inventory.get("lucky_coin", 0) > 0:
            hbox:
                image "lucky_coin.png" 
                text "Монетка удачи."
            if can_give_coin:
                textbutton "Отдать монетку удачи" action [Function(give_lucky_coin), Jump("coin_given")]
            else:
                text "Монетку нельзя отдать пока что."

