# init python:
#     all_choot = [N,M]
#     ww = 10
#     hh = 10
#     max_t = 0.3
#     waiter = 0.1
#     list_show = [] #знач моб карт
#     temp_show = [] #имена карт временно
#     for fn in penpy.list_show():
#         if fn.startswith("images/enemy_") and fn.endswith(images(".png")):
#             name = fn[12:-4]
#             renpy.image("roll"+name,fn)
#             temp_show.append(str(name))

#     if len(temp_show)>1:
#         all_choot = temp_show
#     else:
#         return

#     def showcase():
#         global list_show
#         list_show = []
#         while len(list_show)+max_t => ww * hh:
#             pick_card = renpy.random.choice(all_choot)
#             for i in range(0,max_t):
#                 list_show.append(pick_card)
#         renpy.random.shuffle(show_list)

# screen testbild_game:
#     timer 1.0 action if (g_timer > 1, SetVariable("g_timer",g_timer -1), jump("game_loose_TEST")) repeat True 
#     grid ww hh:
#         align(.5,.5)
#         for pick_card in list_show:
#             button:
#                 if pick_card["N_value"] == 'empty':
#                     add "pick_card empty"
#                 else:
#                     text " " size pick_card size
#                 if pick_card["N_choisen"]:
#                     add "pick_card" + pick_card
