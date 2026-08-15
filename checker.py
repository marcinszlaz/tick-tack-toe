# Dictionaries only for testing purposes.
d = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' _ ', b2=' _ ', b3=' _ ',
         c1=' _ ', c2=' _ ', c3=' _ ',
         quit='quit', name='d only _')

d_x = dict(a1=' _ ', a2=' _ ', a3=' X ',
         b1=' _ ', b2=' _ ', b3=' X ',
         c1=' _ ', c2=' _ ', c3=' X ',
         quit='quit', name='d_x 3[a-c]=X')

d_x_d = dict(a1=' X ', a2=' _ ', a3=' X ',
         b1=' _ ', b2=' X ', b3=' _ ',
         c1=' X ', c2=' _ ', c3=' X ',
         quit='quit', name='d_x_d [c1b2a3|c3b2a1]=X')

d_o = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' _ ', b2=' _ ', b3=' _ ',
         c1=' O ', c2=' O ', c3=' O ',
         quit='quit', name='d_o c[1-3]=O')

d_o_d = dict(a1=' O ', a2=' _ ', a3=' O ',
         b1=' _ ', b2=' O ', b3=' _ ',
         c1=' O ', c2=' _ ', c3=' O ',
         quit='quit', name='d_o_d [a1b2c3|a3b2c3]=O')

dr1 = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' X ', b2=' X ', b3=' X ',
         c1=' _ ', c2=' _ ', c3=' _ ',
         quit='quit', name='dr1 a1^O, b[1-3]^X, c3^O')

set_d1t = set([dr1['a1'], dr1['b2'], dr1['c3']])
set_d2t = set([dr1['a3'], dr1['b2'], dr1['c1']])
tup_chars = ('a', 'b', 'c',)
tup_digits = ('1', '2', '3',)

def check_who_win(dct: dict, who: str, print_=True)->bool:
    """ arg1: dictionary with mapped x,o key names
        a1,a2... c2,c3,
        arg2: who gets two values ' O ' or ' X ',
        arg3: print answer or not,
        function returns True or False """

    set_d1 = set([dct['a1'], dct['b2'], dct['c3']])
    set_d2 = set([dct['a3'], dct['b2'], dct['c1']])
    set_x = set([' X '])
    set_o = set([' O '])
    won = False

    for c in tup_chars:
        for d in tup_digits:
            if dct[c+d] != who:
                won = False
                break
            won = True
        if won:
            break
    if not won:
        for d in tup_digits:
            for c in tup_chars:
                if dct[c+d] != who:
                    won = False
                    break
                won = True
            if won:
                break
    if not won:
        if (set_d1 == (set_x if who == ' X ' else
                        (set_o if who == ' O ' else set() ))):
            won = True
        elif (set_d2 == (set_x if who == ' X ' else
                        (set_o if who == ' O ' else set() ))):
            won = True
        else:
            won = False

    print(f"Did you win: {won}") if print_ else print(f"", end="") 
    return won

def check_draw(d_: dict):
    for c in tup_chars:
        for d in tup_digits:
            if d_[c+d] == ' _ ':
                return False
            else:
               pass 
    print("We\'ve draw!")
    return True

# For testing purposes only.
if __name__ == "__main__":
    check_who_win(d_o, ' O ')
