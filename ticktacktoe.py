import os
import time


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

d = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' _ ', b2=' _ ', b3=' _ ',
         c1=' _ ', c2=' _ ', c3=' _ ')

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

clear_screen()
print(f"Welcome in Tic-Tac-Toe game \n"
     f"Type a1, b3, etc. to fill the board.\n"
     f"Type `quite` to quit\n\n"
     f"{return_game_board()}")

init = 0
user_choose = 'no_quit!'
while user_choose != 'quit':
    if init % 2 == 0:  
        user_choose = input("Player `X` turn! \n")
        d[user_choose] = ' X '
    else:
        user_choose = input("Player `Y` turn! \n")
        d[user_choose] = ' O '
    clear_screen()
    print(game_board_ft.format(**d))
    init += 1





