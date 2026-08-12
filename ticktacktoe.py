import os
import time
from template_rejuvenation import RejuvenatesTemplate
from checker import check_who_win


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

d = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' _ ', b2=' _ ', b3=' _ ',
         c1=' _ ', c2=' _ ', c3=' _ ',
         quit='quit')

# classic f-string, no auto-refresh, it's problem here
# you have use funcion or lambda
game_board = (f"\n" 
f"   A   B   C \n"
f" 1{d['a1']}|{d['b1']}|{d['c1']}\n"
f"  ---|---|---\n"
f" 2{d['a2']}|{d['b2']}|{d['c2']}\n"
f"  ---|---|---\n"
f" 3{d['a3']}|{d['b3']}|{d['c3']}\n"
f"")
return_game_board = lambda: game_board

# intended to use with .format() function
game_board_ft = ("\n" 
"   A   B   C \n"
" 1{a1}|{b1}|{c1}\n"
"  ---|---|---\n"
" 2{a2}|{b2}|{c2}\n"
"  ---|---|---\n"
" 3{a3}|{b3}|{c3}\n")

# set_x, set_y
set_x = (' X ', ' X ', ' X ')
set_y = (' O ', ' O ', ' O ')

clear_screen()
print(f"Welcome in Tic-Tac-Toe game \n"
     f"Type a1, b3, etc. to fill the board.\n"
     f"Type `quit` to quit\n\n"
     f"{return_game_board()}")

init = 0
user_choose = 'no_quit!'
rejuvenate = RejuvenatesTemplate(d, game_board_ft)

while user_choose != 'quit':
    if init % 2 == 0:  
        user_choose = input("Player `X` turn! \n")
        if user_choose not in d:
            if user_choose == 'quit':
                print("Bye")
                print('u', user_choose)
                break
            print("Wrong input!")
            print('u', user_choose)
            continue
        if d[user_choose] == ' _ ':
            d[user_choose] = ' X '
        elif d[user_choose] == ' O ' or ' X ':
            print("You can\'t do that!")
            continue
        else:
            d[user_choose] = ' X '
        clear_screen()
        print(game_board_ft.format(**d))
        (print("Player X wins!") if check_who_win(d, ' X ', False)
         else print('',end=''))
    else:
        user_choose = input("Player `O` turn! \n")
        if user_choose not in d:
            if user_choose == 'quit':
                print("Bye")
                print(user_choose)
                break
            print("Wrong input!")
            print(user_choose)
            continue
        if d[user_choose] == ' _ ':
            d[user_choose] = ' O '
        elif d[user_choose] == ' X ' or ' O ':
            print("You can\'t do that!")
            continue
        else:
            d[user_choose] = ' O '
        clear_screen()
        print(rejuvenate)
        (print("Player O wins!") if check_who_win(d, ' O ', False) 
        else print('',end=''))

    init += 1

