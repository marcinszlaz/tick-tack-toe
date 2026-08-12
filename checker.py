# Dictionaries only for testing purposes.
d = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' _ ', b2=' _ ', b3=' _ ',
         c1=' _ ', c2=' _ ', c3=' _ ',
         quit='quit')

d_x = dict(a1=' _ ', a2=' _ ', a3=' X ',
         b1=' _ ', b2=' _ ', b3=' X ',
         c1=' _ ', c2=' _ ', c3=' X ',
         quit='quit')

d_x_d = dict(a1=' X ', a2=' _ ', a3=' X ',
         b1=' _ ', b2=' X ', b3=' _ ',
         c1=' X ', c2=' _ ', c3=' X ',
         quit='quit')

d_o = dict(a1=' _ ', a2=' _ ', a3=' _ ',
         b1=' _ ', b2=' _ ', b3=' _ ',
         c1=' O ', c2=' O ', c3=' O ',
         quit='quit')

d_o_d = dict(a1=' O ', a2=' _ ', a3=' O ',
         b1=' _ ', b2=' O ', b3=' _ ',
         c1=' O ', c2=' _ ', c3=' O ',
         quit='quit')

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
    tup_chars = ('a', 'b', 'c',)
    tup_digits = ('1', '2', '3',)
    won = False

    for c in tup_chars:
        for d in tup_digits:
            if dct[c+d] != who:
                won = False
                break
            won = True
    if not won:
        for d in tup_digits:
            for c in tup_chars:
                if dct[c+d] != who:
                    won = False
                    break
                won = True
    if not won:
        if set_d1 == (set_x if who == ' X ' else set_o):
            won = True
        elif set_d2 in (set_x if who == ' X ' else set_o):
            won = True
        else:
            won = False

    print(f"Did you win: {won}") if print_ else print(f"", end="") 
    return won

# For testing purposes only.
if __name__ == "__main__":
    vertical(d_o, ' O ')
