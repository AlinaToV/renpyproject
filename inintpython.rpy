
init python:

    items = [("item1"), ("item2"),("item3")]
    last_item = None

    def SelectitemF(index):
        global last_item
        if (index >= 0) and (index < len(items)):
            last_item = items.pop(index)  
            

            if last_item[0] == "lucky_coin":
                renpy.print("Пока нельзя отдать")
            elif last_item[0] == "timer":
                renpy.print("timeofgame")  
            elif last_item[0] == "tesb":
                renpy.print("гг")

 
    def GetFN(index=0):
        if (index >= 0) and (index < len(items)):
            item = items[index]
            if len(item) == 2:  
                fn, nh = item 
                return "inventory" + fn + ".png"  
            else:
                return ""  
            return ""

    def GetHint(index=0):
        if (index >= 0) and (index < len(items)):
            item = items[index] 
            if len(item) == 2:  
                fn, nh = item  
                return nh 
            else:
                return "" 
        else:
            return ""
