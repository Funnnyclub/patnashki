from msvcrt import getch
from os import system
from time import sleep

CODE = 224
up = 72
down = 80
right = 77
left = 75
ENTER = 13
TAB_END = 63
rows = 4
cols = 4
SPACE = 32
SYM = chr(42)
size = 4

def show (lst):
    system('cls')
    print("+------+------+------+------+")
    for i in range(size):
        for j in range(size):
            print('| {:^4}'.format(lst[i][j] if lst[i][j] != 16 else " "), end=" ")
        print("|")
        print("+------+------+------+------+")

def go_up(lst,x,y):
    if y > 0:
        y -= 1
        lst[y][x],lst[y+1][x] = lst[y+1][x],lst[y][x]
    return x,y

def go_down(lst,x,y):
    if y < size - 1:
        y += 1
        lst[y][x], lst[y-1][x] = lst[y-1][x], lst[y][x]
    return x, y

def go_left(lst,x,y):
    if x > 0:
        x -= 1
        lst[y][x], lst[y][x+1] = lst[y][x+1], lst[y][x]
    return x, y
def go_right(lst,x,y):
    if x < size - 1:
        x += 1
        lst[y][x], lst[y][x-1] = lst[y][x-1], lst[y][x]
    return x, y

def step(lst,x,y):
    ch = ord(getch())
    if ch == CODE:
        ch = ord(getch())
        if ch == up:
          return go_up(lst,x,y)
        elif ch == down:
          return go_down(lst,x,y)
        elif ch == left:
          return go_left(lst,x,y)
        elif ch == right:
          return go_right(lst,x,y)
    elif ch == SPACE:
        return None
    else:
        return x,y

def shake(lst,x,y):
    from random import randint
    for _ in range(1000):
        direct = randint(1, 4)
        if direct == 1:
            x,y = go_up(lst,x,y)
        elif direct == 2:
            x,y = go_down(lst,x,y)
        elif direct == 3:
            x,y = go_left(lst,x,y)
        elif direct == 4:
            x,y = go_right(lst,x,y)

    return x,y




def is_win(lst):
    x = 1
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if x == lst[i][j]:
                x += 1
            else:
                return False
    return True


new_field = [[j+1 + i*size for j in range(size)] for i in range(size) ]
show(new_field)

emp_x = size - 1
emp_y = size - 1
sleep(5)
emp_x,emp_y = shake(new_field,emp_x,emp_y)
show(new_field)

while True:
    res = step(new_field,emp_x,emp_y)
    if res is None:
        break
    show(new_field)
    emp_x,emp_y = res

    if is_win(new_field):
        print("Game OVER")
        break


