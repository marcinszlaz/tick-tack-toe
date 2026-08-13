import os
import time
from template_rejuvenation import RejuvenatesTemplate
from checker import check_who_win, tup_chars, tup_digits


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

score_x = 0
score_o = 0
rx = lambda: score_x
ro = lambda: score_o
d = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' _ ', b2=' _ ', b3=' _ ',
         c1=' _ ', c2=' _ ', c3=' _ ',
         quit='quit', x=rx(), o=ro())

def clear_dict(dct: dict)->None:
    """ write ' _ ' values to cells
        a1-c3, update values x, o """
    global score_x, score_o
    for c in tup_chars:
        for d in tup_digits:
            dct[c+d] = ' _ '
    dct['o'] = ro();dct['x'] = rx()
    return None

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
" X: {x}  O: {o}\n\n" 
"   A   B   C \n"
" 1{a1}|{b1}|{c1}\n"
"  ---|---|---\n"
" 2{a2}|{b2}|{c2}\n"
"  ---|---|---\n"
" 3{a3}|{b3}|{c3}\n")

clear_screen()
print(f"Welcome in Tic-Tac-Toe game \n"
     f"Type a1, b3, etc. to fill the board.\n"
     f"Type `quit` to quit\n\n"
     f"{return_game_board()}")
rejuvenate = RejuvenatesTemplate(d, game_board_ft)

def main():
    init = 0
    user_choose = 'no_quit!'
    global score_x, score_o
    while user_choose != 'quit':
        if init % 2 == 0:  
            user_choose = input("Player `X` turn! \n")
            if user_choose not in d:
                if user_choose == 'quit':
                    print("Bye")
                    break
                print("Wrong input!")
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
            if check_who_win(d, ' X ', False):
                score_x += 1 
                print(f"Player X won!")
                _ = input("Again? (y/n)")
                if _.lower() == 'y':
                    clear_dict(d)
                    clear_screen()
                    print(rejuvenate)
                    main()
                else:
                    print("Bye!")
                    time.sleep(0.5)
                    user_choose = 'quit'
            else:
                print(f"", end='')
        else:
            user_choose = input("Player `O` turn! \n")
            if user_choose not in d:
                if user_choose == 'quit':
                    print("Bye")
                    break
                print("Wrong input!")
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
            if check_who_win(d, ' O ', False):
                score_o += 1 
                print(f"Player O won!")
                _ = input("Again? (y/n)")
                if _.lower() == 'y':
                    clear_dict(d)
                    clear_screen()
                    print(rejuvenate)
                    main()
                else:
                    print("Bye!")
                    time.sleep(0.5)
                    user_choose = 'quit'
            else:
                print(f"", end='')
        init += 1
main()
