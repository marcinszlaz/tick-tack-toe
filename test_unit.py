# Test unit for checker.py module
# Circular import alert!

from checker import * 

dct_list = [d, d_x, d_x_d, d_o, d_o_d, dr1] 
def chch(dct_: list = dct_list, who: str = ' X ')->bool:
    for d in dct_:
        print(f"dict_name: {d['name']} checked: {who}")
        check_who_win(dct=d, who=who,print_=True)

if __name__ == "__main__":
    chch()
