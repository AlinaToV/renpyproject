init -2 python:
    items = []
    last_item = None

    def SelectitemF(index):
        if (index >= 0) and (index < len(items)):
            last_item = items.pop(index)
            renpy.restart_interaction()
            if last_item[0] == "lucky_coin":
                renpy.print("Пока нельзя отдать")
            if last_item[0] == "timer":
                renpy.print("timeofgame")#подвезти потом таймер
            Selectitem = renpy.curry(SelectitemF)

    def GetFN(index=0):
        global items
        if (index >= 0) and (index < len(items)):
            fn, nh = items[index]
            return "inventory/"+ fn + ".png"
        else:
            return ""
    
    def GetHint(index = 0):
        global items
        if (index >= 0) and (index < len(items)):
            fn,nh = items[index]
            return nh
        else:
            return ""