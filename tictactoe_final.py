def main():
    pass

if __name__ == '__main__':
    main()

field = [' '] * 9
current = 'X'

def display():
    print('---------')
    print('|', field[0], field[1], field[2], '|')
    print('|', field[3], field[4], field[5], '|')
    print('|', field[6], field[7], field[8], '|')
    print('---------')

def reverse_char():
    global current
    if current == 'X':
        current = 'O'
    else:
        current = 'X'

def replace_xo(old, ind):
    global current
    new = list(old)
    new[ind] = current
    reverse_char()
    return ''.join(new)

def do_move(ui, nm):
    global field
    address = ['1 3', '2 3', '3 3', '1 2', '2 2', '3 2', '1 1', '2 1', '3 1']
    nm = nm.split()
    if len(nm) == 2:
        if nm[0].isdigit() and nm[1].isdigit():
            if (0 < int(nm[0]) < 4) and (0 < int(nm[1]) < 4):
                move = address.index(' '.join(nm))
                if field[move] != ' ':
                    print('This cell is occupied! Choose another one!')
                    do_move(field, input('Enter the coordinates:'))
                else:
                    field = replace_xo(field, move)
                    display()
            else:
                print('Coordinates should be from 1 to 3!')
                do_move(field, input('Enter the coordinates:'))
        else:
            print('You should enter numbers!')
            do_move(field, input('Enter the coordinates:'))
    else:
        print('You should enter numbers!')
        do_move(field, input('Enter the coordinates:'))

def win_check(win):
    if (win[0] == win[1] == win[2] != ' ') or \
       (win[0] == win[3] == win[6] != ' ') or \
       (win[0] == win[4] == win[8] != ' ') or \
       (win[1] == win[4] == win[7] != ' ') or \
       (win[2] == win[4] == win[6] != ' ') or \
       (win[2] == win[5] == win[8] != ' ') or \
       (win[3] == win[4] == win[5] != ' ') or \
       (win[6] == win[7] == win[8] != ' '):
        return True
    return False

def is_draw(draw):
    for _ in draw:
        if _ == ' ':
            return False
    if  win_check(draw):
        return False
    return True

def what_happened():
    if is_draw(field):
        print('Draw')
    if win_check(field):
        reverse_char()
        print(current, 'wins')


display()
while not (win_check(field) or is_draw(field)):
    do_move(field, input('Enter the coordinates:'))
what_happened()
